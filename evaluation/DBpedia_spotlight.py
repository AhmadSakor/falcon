# -*- coding: utf-8 -*-

import requests
import csv
import evaluation


def dbpeida_spotlight_call(text):
    print(text)
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get('https://api.dbpedia-spotlight.org/en/annotate?text='+text, headers=headers)
    if response.status_code == 200:
        result=response.json()
        if 'Resources' in result:
            return result['Resources']
        else:
            return ""
    else:
        temp=dbpeida_spotlight_call(text)
        return temp


if __name__ == "__main__":
    questions=evaluation.read_LCQUAD()
    #questions=evaluation.read_LCQUAD2()
    #questions=evaluation.read_QALD7()
    
    
count=1
for question in questions:    
    p_relation=0
    r_relation=0
    p_entity=0
    r_entity=0
    print(count)
    print(question[0])
    results=dbpeida_spotlight_call(question[0])
    results=[result['@URI'] for result in results]
    entities=results
    

    print(entities)
    

    
    numberSystemEntities=len(question[3])
    intersection= set(question[3]).intersection(entities)
    if numberSystemEntities!=0 and len(entities)!=0 :
        p_entity=len(intersection)/len(entities)
        r_entity=len(intersection)/numberSystemEntities
    question.append(entities)
    question.append(p_entity)   
    question.append(r_entity)   
    '''for relation in question[2]:
        if relation in relations:
            correctRelations=correctRelations+1
        else:
            wrongRelations=wrongRelations+1
    for entity in question[3]:
        if entity in entities:
            correctEntities=correctEntities+1
        else:
            wrongEntities=wrongEntities+1'''
    count=count+1

with open('data/Spotlight_LCQUAD.csv',  mode='w' ) as results_file:
    writer=csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for question in questions:
        if len(question)==4:
            question.append([])
            question.append([])
            question.append(0)
            question.append(0)
            question.append(0)
            question.append(0)
        writer.writerow([question[0],question[3],question[4],question[5],question[6]])
        
  
