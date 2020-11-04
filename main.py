import os 

file = '/bestsellers.txt'
path = os.getcwd()+file
raw = open(path,'r+')
content = raw.read()

content = content.strip().split('\n')

dat = list()

for i in content:
    dat.append(i.split('\t'))

print(dat, path)
