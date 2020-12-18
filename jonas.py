import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

### import the text file
# define path
file = '/bestsellers.txt'
path = os.getcwd() + file

# open it
fp = open(path, 'r+')

# read the content
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
df = pd.DataFrame(doc, columns=['Title', 'Author', 'Publisher', 'Date', 'Category'])

# take the date column as index, for easier filtering later -> show just the date and not the time
df.index = pd.to_datetime(df.Date).dt.date

# remove the column date, otherwise it would be double
df.drop('Date', inplace=True, axis=1)


# Enter a title a title or part of a title and find the book
def search_for_title():
    # enter a tile
    s_title = input("Enter a title or a part of a title: ")
    # look for the the rows which contain the title (type: str) entered, disable case sensitivity
    df_title = df[df.Title.str.contains(s_title, case=False)]
    # if the df doesn't contain any entries, display an error-message
    if df_title.empty:
        print("sorry, we couldn't find a book with this title\n")
    # if books are found, print it out using to_markdown for a nicer presentation. remove the category column
    else:
        print('\nHere all the books you are looking for:\n', '\n', df_title.drop('Category', axis=1).to_markdown())


# plot publishers by silvan
def plot_publishers():
    # select startdate
    y_from = str(input(
        f'In which year you want to start? (enter a year between {df.index.min().year} and {df.index.max().year}) '))

    # select enddate
    y_to = str(input(f'In which year you want to end? (enter a year between {y_from} and {df.index.max().year}) '))

    # count bestsellers per publisher
    pub_count = df.loc[y_from:y_to]['Publisher'].value_counts()

    # set the limit of how many publisher you want to see
    limit = int(input(f'How many publisher do you want to see? (enter a value between 1 and {len(pub_count)}) '))

    # return barplot
    return (pub_count[:limit].plot.bar())

    plt.show()

    df.Category.count_values


# choose one of the options:
while True:
    print("\nWhat would you like to do?\n"
          "\n1: Look up year range\n"
          "2: Look up month/year\n"
          "3: Search for author\n"
          "4: Search for title\n"
          "5: Plot the Publishers in a chosen time frame\n"
          "Q: Quit\n")

    decision = input("Enter your decision: ")

    if "4" == decision:  # !! change to elif !!
        search_for_title()
    elif '5' == decision:
        plot_publishers()
    elif "q" == decision or decision == "Q":
        sys.exit('Goodbye and have a nice day!')
    else:
        print('please choose one of the given options')

