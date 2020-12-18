import os
import tabulate
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
df = pd.DataFrame(
    doc, columns=['Title', 'Author', 'Publisher', 'Date', 'Category'])

# take the date column as index, for easier filtering later -> show just the date and not the time
df.index = pd.to_datetime(df.Date)

# remove the column date, otherwise it would be double
df.drop('Date', inplace=True, axis=1)


## this is a helper function for year inputs
def input_year_range(d=df):
    # select startdate
    y_from = str(
        input(
            f'In which year you want to start? (enter a year between {d.index.min().year} and {d.index.max().year}) \n'
        ))
    # select enddate
    y_to = str(
        input(
            f'In which year you want to end? (enter a year between {y_from} and {d.index.max().year}) \n'
        ))
    # return inputs
    return (y_from, y_to)


## function to serach titles in a year range (menu option 1)
def year_range():
    try:
        #Ask for starting and ending year
        StartingYear = int(
            input(
                '\n\tPleaser enter the starting year (between 1942 and 2013) here: '
            ))
        EndingYear = int(
            input(
                '\tPleaser enter the ending year (between 1942 and 2013) here: '
            ))

        #Empty list that is filled with entries that reached #1 between the entered years
        Yearlist = []

        #Split the dates of all entrys into a list [day, month, year]
        for i in doc:
            YearIs = i[3].split('/')

            #print entry is year of entry is between the starting year and the ending year
            if int(YearIs[2]) >= StartingYear and int(YearIs[2]) <= EndingYear:
                Yearlist.append(i)

        #Check whether list has entrys
        #If so: print list
        if len(Yearlist) > 0:
            print('\nAll titles between %s' % StartingYear + ' and ' +
                  '%s: ' % EndingYear)
            for i in Yearlist:
                print(', '.join(i))

        #If not: print message that no entry could be found
        else:
            print('\n***Sorry, we could not find anything***')

    except:
        print('\n***ERROR - Please enter a number***')


## function to serach titles in specific year and month (menu option 2)
def month_year():
    try:
        #Ask for year and month
        year = int(
            input(
                '\n\tWhat year are you looking for? (enter a year between 1942 and 2013) '
            ))
        month = int(input('\tWhich month? (enter a number between 1 an 12) '))

        #Empty list that is filled with entries that reached #1 in the entered  year and month
        Datelist = []

        #Split the dates of all entries into a list [day, month, year]
        for i in doc:
            DateIs = i[3].split('/')

            #print entry if entry is in month and year
            if int(DateIs[2]) == year and int(DateIs[0]) == month:
                Datelist.append(i)

        #Check whether list has entrys
        #If so: print list
        if len(Datelist) > 0:
            print('\nIn %d/%d the following titles were bestsellers:' % (month,
                                                                         year))
            for i in Datelist:
                print(', '.join(i))

        #If not: print message that no entry could be found
        else:
            print('\n***Sorry, we could not find anything***')

    #Error message if user didn't enter a number
    #Loop doesn't break until user enters numbers
    except:
        print('\n***ERROR - Please enter a number***')


## function to serach titles by author name (menu option 3)
def search_for_author():
    # mutate index for better readability of the output
    df.index = pd.Series(df.index).dt.date
    #Prompt user to enter an author search term
    s_author = input("Enter the name of an author or part of a name: ")
    #Look for the rows in the Author data that contain the author the user searched for, removing case sensitivity
    df_author = df[df.Author.str.contains(s_author, case=False)]
    #If no author is found for the search, display error-message
    if df_author.empty:
        print("Sorry, we could not find a book with this author")
    #If an author is found, print the title, author, publisher, date
    else:
        print("\nHere is the author you are looking for and their work:\n",
              "\n",
              df_author.drop('Category', axis=1).to_markdown())


## function to serach books by title or part of a title (menu option 4)
def search_for_title():
    # mutate index for better readability of the output
    df.index = pd.Series(df.index).dt.date
    # enter a tile
    s_title = input("Enter a title or a part of a title: ")
    # look for the rows which contain the title (type: str) entered, disable case sensitivity
    df_title = df[df.Title.str.contains(s_title, case=False)]
    # if the df doesn't contain any entries, display an error-message
    if df_title.empty:
        print("sorry, we couldn't find a book with this title\n")
    # if books are found, print it out using to_markdown for a nicer presentation. remove the category column
    else:
        print(
            '\nHere are all the books you are looking for:\n', '\n',
            df_title.drop('Category',
                          axis=1).to_markdown(disable_numparse=True))


## function to serach publishers with most bestsellers in a year range (menu option 5)
def plot_publishers():
    df.index = pd.to_datetime(df.index)
    # get years
    y_from, y_to = input_year_range()
    # count bestsellers per publisher
    pub_count = df.loc[y_from:y_to]['Publisher'].value_counts()

    # set the limit of how many publisher you want to see
    limit = int(
        input(
            f'How many publisher do you want to see? (enter a value between 1 and {len(pub_count)}) '
        ))
    # return barplot
    return (pub_count[:limit].plot.bar())


def clear():
    # clear screen
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')


clear()
# choose one of the options:
while True:
    print("\nWhat would you like to do?\n"
          "\n1: Look up a year range\n"
          "2: Look up month/year\n"
          "3: Search for author\n"
          "4: Search for title\n"
          "5: Plot the Publishers in a chosen time frame\n"
          "Q: Quit\n")

    decision = input("Enter your decision: ")

    try:
        if decision == '1':
            year_range()
        elif decision == '2':
            month_year()
        elif decision == '3':
            search_for_author()
        elif decision == '4':
            search_for_title()
        elif decision == '5':
            plot_publishers()
            plt.show(block=False)
        elif decision.lower() == 'q':
            print("Goodbye and have a nice day!")
            break
        else:
            print('please choose one of the given options')
    except:
        print('\n***Ooops - something went wrong***\n'
              'Did you type the input in the correct format?')

    # this "do you want to continue" message is, that the user can read the output before continuing
    will_to_continue = input('\nDo you want to continue(y/n)? ')
    if will_to_continue.lower() == 'y':
        clear()
    elif will_to_continue.lower() == 'n':
        clear()
        break
