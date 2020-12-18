#Prompt user to input author they want to search for
author_search = input('Input author search term: ')
#Search for author in dataset and return the author along with the book title
for book in doc:
  if author_search in book[1]:
    print(book[0],', ','by ',book[1])

#Prompt user to input title they want to search for
title_search = input('Input title search term: ')
#Search for book and return the title along with the author
for book in doc:
  if title_search in book[0]:
    print('"',book[0],'"','by ',book[1])

## function to serach titles by author name (menu option 3)
def search_for_author(): 
  #Prompt user to enter an author search term
  s_title=input("Enter the name of an author or part of a name: ")
  #Look for the rows in the Author data that contain the author the user searched for, removing case sensitivity
  df_author=df[df.Author.str.contains(s_author,case=False)]
  #If no author is found for the search, display error-message
  if df_author.empty:
    print("Sorry, we could not find a book with this author")
  #If an author is found, print the title, author, publisher, date 
  else:
    print("\nHere is the author you are looking for and their work:\n", "\n", df_author.drop('Category', axis=1).to_markdown())