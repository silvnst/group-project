import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
# import matplotlib
import pandas

file='/bestsellers.txt'
path=os.getcwd()+file
fp=open(path,'r+')
content = fp.read()

### pharse txt file

# lines are separated by '\n'
content = content.split('\n')

## the words are separeted by tabs '\t', so we separate those as well

# initiate list for result
doc = list()

# separate the values of each line of the original txt document
for i in content:
    doc.append(i.split('\t'))

# transfer the data to a nice pandas.DataFrame, so data manipulation (count values) gets easier
df = pandas.DataFrame(doc, columns = ['Title', 'Author', 'Publisher', 'Date', 'Category'])

# take the date column as index, for easier filtering later
df.index = pd.to_datetime(df.Date)

### function to get the to bestsellers in the given time

def plot_publishers():
    
    # select startdate
    y_from = int(input(f'In which year you want to start? (enter a year between {df.index.min().year} and {df.index.max().year}) '))
    
    # select enddate
    y_to = int(input(f'In which year you want to end? (enter a year between {y_from} and {df.index.max().year}) '))
    
    # count bestsellers per publisher
    pub_count = df[str(y_from):str(y_to)]['Publisher'].value_counts()
    
    # set the limit of how many publisher you want to see
    limit = int(input(f'How many publisher do you want to see? (enter a value between 1 and {len(pub_count)}) '))
    
    # make the barplot
    pub_count.plot.bar()
