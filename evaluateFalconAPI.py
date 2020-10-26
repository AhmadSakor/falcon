# -*- coding: utf-8 -*-
import requests
from evaluation import evaluation_paper as evaluation
import csv



headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}







    
def falcon_call(text):
    url = 'https://labs.tib.eu/falcon/api?mode=long'
    entities=[]
    relations=[]
    payload = '{"text":"'+text+'"}'
    r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
    if r.status_code == 200:
        response=r.json()
        for result in response['entities']:
            try:
                entities.append(result[0])
            except:
                continue
        for result in response['relations']:
            try:
                relations.append(result[0])
            except:
                continue
    else:
        r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
        if r.status_code == 200:
            response=r.json()
            for result in response['entities']:
                try:
                    entities.append(result[0])
                except:
                    continue
            for result in response['relations']:
                try:
                    relations.append(result[0])
                except:
                    continue
            
    return entities,relations

def evaluate(entities_falcon,relations_falcon, entities_goldstandard,relations_goldstandard):
    p_entity = 0
    r_entity = 0
    p_relation = 0
    r_relation = 0
    
    '''for i in range(len(entities_falcon)):
        entities_falcon[i]= entities_falcon[i][entities_falcon[i].rfind('/')+1:-1]
        
    for i in range(len(relations_falcon)):
        relations_falcon[i]= relations_falcon[i][relations_falcon[i].rfind('/')+1:-1]'''
        
    falocn_relations=[x[x.rfind('/')+1:-1] for x in relations_falcon]
    gold_relations=[x[x.rfind('/')+1:-1] for x in relations_goldstandard]
    numberSystemEntities = len(entities_goldstandard)
    if numberSystemEntities==0:
        p_entity=1
        r_entity=1
    else:
        intersection = set(entities_goldstandard).intersection(entities_falcon)
        if len(entities_falcon) != 0:
            p_entity = len(intersection) / len(entities_falcon)
        r_entity = len(intersection) / numberSystemEntities
    
    ################################################################
    numberSystemRelations = len(gold_relations)
    if numberSystemRelations==0:
        p_relation=1
        r_relation=1
    else:
        intersection = set(gold_relations).intersection(falocn_relations)
        if len(falocn_relations) != 0:
            p_relation = len(intersection) / len(falocn_relations)
        r_relation = len(intersection) / numberSystemRelations


    return p_entity, r_entity , p_relation, r_relation

result = []
result.append(["Question", "Gold Standard Entities", "Gold Standard Relations", "FALCON_Entities","P_E", "R_E","FALCON_Relations","P_R","R_R"])
questions = evaluation.read_QALD7()
#questions = evaluation.read_LCQUAD()
#questions = evaluation.read_LCQUAD2()


counter = 0
for question in questions[:10]:
    if len(question[1])==0:
        continue
    entities_falcon,relations_falcon = falcon_call(question[0])        
    p_e, r_e, p_r , r_r = evaluate(entities_falcon, relations_falcon,question[3],question[2])
    result.append([question[0], question[3], question[2],entities_falcon, p_e, r_e ,relations_falcon, p_r , r_r])
    print(str(counter))
    counter = counter + 1
    
with open('datasets/falcon_qald7.csv', mode='w', newline='', encoding='utf-8') as results_file:
    writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(result)
