import os 

file = '/bestsellers.txt'
path = os.getcwd()+file
raw = open(path,'r+')
content = raw.read()

content = content.strip().split('\n')



dat = list()

for i in content:
  dat.append(i.split('\t'))

while True:
  #Ask the Questions that user has to answer
  Questions = ['What would you like to do?', '\n1: Look up year range', '\n2: Look up month/year','\n3: Search for author','\n4: Search for title', '\nC: Close the program']

  print('\n')
  for i in Questions:
    print(i.strip())

  #User input
  UserInput = input('\nPlease enter your choice here: ')

#Option 1
  if UserInput == '1':

    #While loop that breaks if user enters valid input (i.e. numbers)
    while True:
    
      try:
        #Ask for starting and ending year
        StartingYear = int(input('\n\tPleaser enter the starting year here: '))
        EndingYear = int(input('\tPleaser enter the ending year here: '))
        
        #Empty list that is filled with entries that reached #1 between the entered years
        Yearlist = []

        #Split the dates of all entrys into a list [day, month, year]
        for i in dat:
          YearIs = i[3].split('/')

          #print entry is year of entry is between the starting year and the ending year
          if  int(YearIs[2]) >= StartingYear and int(YearIs[2]) <=   EndingYear:
            Yearlist.append(i)    

        #Check whether list has entrys
        #If so: print list    
        if len(Yearlist) > 0:
          print('\nAll titles between %s' % StartingYear + ' and ' + '%s: ' %EndingYear)
          for i in Yearlist:
            print(', '.join(i))

          #Break loop to get back to starting menu
          break
        
        #If not: print message that no entry could be found
        else:
          print('\n***Sorry, we could not find anything***')

          #Break loop to get back to starting menu
          break
    
      #Error message if user didn't enter a number
      #Loop doesn't break until user enters numbers
      except:
        print('\n***ERROR - Please enter a number***')

  #Option 2
  if UserInput == '2':

    #While loop that breaks if user enters valid input (i.e. numbers)
    while True:
    
      try:
        #Ask for year and month
        year = int(input('\n\tWhat year are you looking for? '))
        month = int(input('\tWhich month? '))
        
        #Empty list that is filled with entries that reached #1 in the entered  year and month
        Datelist = []

        #Split the dates of all entries into a list [day, month, year]
        for i in dat:
          DateIs = i[3].split('/')
          

          #print entry if entry is in month and year
          if  int(DateIs[2]) == year and int(DateIs[0]) == month:
            Datelist.append(i)    

        #Check whether list has entrys
        #If so: print list    
        if len(Datelist) > 0:
          print('\nIn %d/%d the following titles were bestsellers:' % (month, year))
          for i in Datelist:
            print(', '.join(i))

          #Break loop to get back to starting menu
          break
        
        #If not: print message that no entry could be found
        else:
          print('\n***Sorry, we could not find anything***')

          #Break loop to get back to starting menu
          break
    
      #Error message if user didn't enter a number
      #Loop doesn't break until user enters numbers
      except:
        print('\n***ERROR - Please enter a number***')
        
  #Loop breaks and program quits if user enters C/c
  elif UserInput == 'C' or UserInput == 'c':
    print('\n\t***You have quit the program***')
    break

  #If user enters a number/letter that is not [1,2,3,4,C]
  elif UserInput != ['1','2','3','4','C','c']:
    print('\n\t***Input invalid***')