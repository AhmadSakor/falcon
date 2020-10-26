# -*- coding: utf-8 -*-
import evaluation_paper as evaluation
import requests
import csv

headers = {
    'Content-Type': 'application/json',
}


#questions=evaluation.read_LCQUAD()
questions=evaluation.read_LCQUAD2()
#questions=evaluation.read_QALD7()
#questions=evaluation.read_QALD5()
#questions=evaluation.read_QALD6()

count=1
for question in questions:    
    p_relation=0
    r_relation=0
    p_entity=0
    r_entity=0
    print(count)
    print(question[0])
    #data = '{"nlquery":"'+question[0]+'","pagerankflag": false}'
    #data=data.encode("utf-8")
    url="https://tagme.d4science.org/tagme/tag?lang=en&gcube-token=bbcf7be9-ad39-487c-9872-6b1bbc77baf1-843339462&text="+question[0]
    response = requests.post(url)
    if response.status_code != 200:
        continue
    #print(response)
    
    results=response.json()
    #print(results)

    entities=[]
    
    for result in results["annotations"]:
        if result['rho'] > 0.2:
            entities.append("http://dbpedia.org/resource/"+result["title"].replace(" ","_"))
    #print(relations)
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

with open('data/TagMe_LCQUAD-2.csv',  mode='w' ) as results_file:
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
        
  
