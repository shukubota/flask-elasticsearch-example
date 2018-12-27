import os
from elasticsearch import Elasticsearch

dirname = "gutenberg"

es = Elasticsearch()

print(os.listdir(dirname))
print(enumerate(os.listdir(dirname)))

for id, fname in enumerate(os.listdir(dirname)):
  print(id)
  print(fname)
  text, title, author = '', '', ''

  with open(os.path.join(dirname, fname), 'rt') as f:
    header = True
    for line in f:
      if not header:
        text += line
      elif line.startswith('*** START OF THIS PROJEC'):
        header = False
      elif line.startswith('Title:'):
        title = line.split(':')[1].strip()
      elif line.startswith('Author:'):
        author = line.split(':')[1].strip()

  doc = { 'text': text, 'title': title, 'author': author, 'file_name': fname }
  es.index(index='gutenberg_books', doc_type='gutenberg', id=id+1, body=doc)