from elasticsearch import Elasticsearch

es = Elasticsearch()
res = es.search(index='gutenberg_books', body={'_source': ['title', 'author'], 'query': {'match': {'text':'Bennet'}}})

#print(res['hits']['hits'].count)
for doc in res['hits']['hits']:
  print(doc['_source'])