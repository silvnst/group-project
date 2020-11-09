import requests
import json

api = 'wVR4npTI46td45CDTv3uLgyprnbrmpzb'
url = 'https://api.nytimes.com/svc/books/v3/lists.json'
x = '/lists/2019-01-20/hardcover-fiction.json'
r = requests.get(url)

headers = {'Authorization':'Bearer ' + api}
req = requests.request('GET', 'https://httpbin.org/get', headers = headers)

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
