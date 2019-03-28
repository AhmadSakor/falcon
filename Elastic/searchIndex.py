from elasticsearch import Elasticsearch


es = Elasticsearch(['http://localhost:9200'])
docType = "doc"



def entitySearch(query):
    indexName = "dbentityindex"
    results=[]
    ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "prefix" : { "uri" : "http://dbpedia.org/resource/"+query.capitalize().replace(" ", "_") } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/resource/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,40])
        elif  "_" in result["_source"]["uri"] and result["_source"]["uri"].lower()[:result["_source"]["uri"].index("_")]=="http://dbpedia.org/resource/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,30])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*10,0])
        ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "match" : { "uri" : "http://dbpedia.org/resource/"+query.capitalize().replace(" ", "_") } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/resource/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*20,0])
        ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "match" : { "label" : query } 
              }
               ,"size":10
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/resource/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*40,0])
    ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "fuzzy" : { "label" : query  } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/resource/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*25,0])
    return results
    #for result in results['hits']['hits']:
        #print (result["_score"])
        #print (result["_source"])
        #print("-----------")
        
        
        
def ontologySearch(query):
    indexName = "dbontologyindex"
    results=[]
    ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "prefix" : { "uri" : "http://dbpedia.org/ontology/"+query.replace(" ", "_") } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/ontology/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*10,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*10,0])
        ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "match" : { "uri" : "http://dbpedia.org/ontology/"+query.replace(" ", "_") } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/ontology/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*20,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*20,0])
        ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "match" : { "label" : query } 
              }
               ,"size":10
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/ontology/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*40,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*40,0])
    ###################################################
    elasticResults=es.search(index=indexName, doc_type=docType, body={
              "query": {
                "fuzzy" : { "label" : query  } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["uri"].lower()=="http://dbpedia.org/ontology/"+query.replace(" ", "_").lower():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*25,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*25,0])
    return results
    #for result in results['hits']['hits']:
        #print (result["_score"])
        #print (result["_source"])
        #print("-----------")
        
def classSearch(query):
    indexName = "dbclassindex"
    results=[]
    elasticResults=es.search(index=indexName, doc_type=docType, body={
            "query": {
        "bool": {
            "must": {
                "bool" : { "should": [
                      { "multi_match": { "query": "http://dbpedia.org/ontology/"+query.replace(" ", "") , "fields": ["uri"]  }},
                      { "multi_match": { "query": query , "fields": ["label"] , "fuzziness": "AUTO" }},
            ]}
            }
        }
    }
            ,"size":5
    })
    #print(elasticResults)
    for result in elasticResults['hits']['hits']:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"],0])
    return results
    #for result in results['hits']['hits']:
        #print (result["_score"])
        #print (result["_source"])
        #print("-----------")
        
        
def propertySearch(query):
    indexName = "dbpropertyindex"
    results=[]
    elasticResults=es.search(index=indexName, doc_type=docType, body={
            "query": {
        "bool": {
            "must": {
                "bool" : { "should": [
                      { "multi_match": { "query": query , "fields": ["label"]  }},
                      { "multi_match": { "query": "http://dbpedia.org/property/"+query.replace(" ", "") , "fields": ["uri"] , "fuzziness": "AUTO"}} ] }
            }
        }
    }
            ,"size":10})
    for result in elasticResults['hits']['hits']:
        results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*2,0])
    return results
    #for result in results['hits']['hits']:
        #print (result["_score"])
        #print (result["_source"])
        #print("-----------")

