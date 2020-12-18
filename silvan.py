import os 
import pandas as pd

file='/bestsellers2.txt'
path=os.getcwd()+file
fp=open(path,'r+')
content = fp.read()

content = content.split('\n')

doc = list()

for i in content:
    doc.append(i.split('\t'))

df = pd.DataFrame(doc, columns = ['Title', 'Author', 'Publisher', 'Date', 'Category'])
df.index = pd.to_datetime(df.Date)

def plot_publishers():
    y_from = int(input(f'In which year you want to start (enter a year between {df.index.min().year} and {df.index.max().year})? '))
    y_to = int(input(f'In which year you want to end (enter a year between {y_from} and {df.index.max().year})? '))
    limit = 10
    pub_count = df[str(y_from):str(y_to)]['Publisher'].value_counts()[:limit]
    pub_count.plot.bar()

plot_publishers()

#############


import requests
import json

api = 'wVR4npTI46td45CDTv3uLgyprnbrmpzb'
url = 'https://api.nytimes.com/svc/books/v3/lists.json'
x = '/lists/2019-01-20/hardcover-fiction.json'


headers = {'Authorization':'Bearer ' + api}
r = requests.get(url, headers = headers)


import os 
import numpy as np

file = '/bestsellers.txt'
path = os.getcwd()+file
raw = open(path,'r+')
content = raw.read()

content = content.strip().split('\n')

dat = list()

for i in content:
    dat.append(i.split('\t'))




or bestseller in dat:
  all_pub.append(bestseller[3])

# dictionary with all publishers and 
best_of = array()
#pd.DataFrame(columns = ['publisher', 'n_bestsellers'])

i = 0
for pub in set(all_pub):
  best_of(i, 0) = pub
  best_of(i, 1) = all_pub.count(pub)
  i += 1

best_of_df = pd.DataFrame(best_of, columns = ['publisher', 'n_bestsellers'])
best_of_df.sort_values(key = n_bestsellers)
