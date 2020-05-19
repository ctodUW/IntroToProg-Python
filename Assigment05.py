# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CTodhunter, 5.18.2020, changed objFile to strFile because it was bothering me
# CTodhunter, 5.18.2020, finally got the dictionary to populate via page 8 in mod05 notes
# CTodhunter, 5.18.2020, added table formatting to print the lstTable nicely
# CTodhunter, 5.18.2020, got option 2 working
# CTodhunter, 5.18.2020, got option 3 working
# CTodhunter, 5.18.2020, got option 4 working
# CTodhunter, 5.18.2020, commented code
# -------------------------------------------------------------------------#

# -- Data -- #
# declare variables and constants
strFile = 'C:\\_PythonClass\\Assignment05\\ToDoList.txt' # defines object file name
objFile = '' # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstRow = []   # A list for each row
strMenu = ""   # A menu of user options
strChoice = ""   # A Capture the user option selection
intSpace = 30 # variable to help format my table output

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# pulling each row from ToDoList.txt, adding to a dictionary, then appending each dicRow to lstTable
objFile = open(strFile, 'r')

for row in objFile:
    lstRow = row.split(',')
    dicRow = {'Task':lstRow[0],'Priority':lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # printing the header with formatting
        print('Task' + '-'*intSpace + 'Priority')

        #stepping through each row in lstTable
        for dicRow in lstTable:

            # correcting spacing for table formatting
            intDif = intSpace - len(dicRow['Task']) + 10

            # outputting dictionary keys and values for each row
            print(dicRow['Task'] + '-'*intDif + dicRow['Priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        # setting max list items to 10 because I don't like doing to much at once
        if len(lstTable) >= 10:
            print('You have too much on your plate, try removing an item first!')
        else:
            # grabbing user task name and priority level
            strTask = input('Type the task to add it: ')
            strPriority = input('Type the associated priority on a scale of [1-10]: ')

            # adding user data to dicRow
            dicRow = {'Task': strTask, 'Priority': strPriority}
            lstTable.append(dicRow)
            print(f'Task: {strTask} has been added with Priority: {strPriority}')

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        # grabbing user task to remove
        strRemove = input('Type a task name to remove it: ')

        # stepping through lstTable to see if strRemove present, and removing if so
        for row in lstTable:
            if strRemove.lower() == row['Task'].lower():
                lstTable.remove(row)
                print(f'Task: {strRemove} has been removed!')
            else:
                continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

        print('Data from session written to file!')

        objFile = open(strFile, 'w')

        # writting data to strFile that fit's my format for reading the file above
        for row in lstTable:
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        print('See you later!')
        break  # and Exit the program
