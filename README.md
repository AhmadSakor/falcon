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


# Cite our work

```
@inproceedings{conf/naacl/SakorMSSV0A19,
  added-at = {2019-06-07T00:00:00.000+0200},
  author = {Sakor, Ahmad and Mulang, Isaiah Onando and Singh, Kuldeep and Shekarpour, Saeedeh and Vidal, Maria-Esther and Lehmann, Jens and Auer, Sören},
  biburl = {https://www.bibsonomy.org/bibtex/2b71b43be4bf953384eec726d0067f109/dblp},
  booktitle = {NAACL-HLT (1)},
  crossref = {conf/naacl/2019-1},
  editor = {Burstein, Jill and Doran, Christy and Solorio, Thamar},
  ee = {https://aclweb.org/anthology/papers/N/N19/N19-1243/},
  interhash = {2289c18c59f008d36727a0664c2ea1c3},
  intrahash = {b71b43be4bf953384eec726d0067f109},
  isbn = {978-1-950737-13-0},
  keywords = {dblp},
  pages = {2336-2346},
  publisher = {Association for Computational Linguistics},
  timestamp = {2019-06-08T11:38:37.000+0200},
  title = {Old is Gold: Linguistic Driven Approach for Entity and Relation Linking of Short Text.},
  url = {http://dblp.uni-trier.de/db/conf/naacl/naacl2019-1.html#SakorMSSV0A19},
  year = 2019
}

```

![alt text](https://labs.tib.eu/falcon/static/img/logo.jpg "Logo")



