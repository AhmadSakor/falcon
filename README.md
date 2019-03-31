# FALCON

FALCON is an entity and relation linking framework over DBpedia.
FALCON identifies the relations and entities in a short text or question. Then link them to their corresponding URI in DBpedia knowledge graph.


[Demo with API](https://labs.tib.eu/falcon/)


To run the framework. You should first have an elasticsearch endpoint, and a DBpedia endpoint.
The elasticsearch dump can be found here:
[Elastic Dump](https://drive.google.com/file/d/1z9azmdYgpV-vqlSFBruyAmxQ0FVCpvjg/view?usp=sharing)

DBpedia endpoint must be changes in main.py

`dbpediaSPARQL="http://node1.research.tib.eu:4001/sparql"`

`dbpediaSPARQL2="http://node1.research.tib.eu:4001/sparql"`

Also Elasticsearch endpoint should be changes in Elastic/searchIndex.py:

`es = Elasticsearch(['http://localhost:9200'])`

Then the function evaluate can be called to process a question.

FALCON benchmariking for QALD-7 dataset using GERBIL

[GERBIL](http://gerbil.aksw.org/gerbil/experiment?id=201812110001)


![alt text](https://labs.tib.eu/falcon/static/img/logo.jpg "Logo")



