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

