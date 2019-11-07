# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KBhattarai,11/5/2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"            # An object that represents a file
strData =''                         # A row of text data from the file



dicRow = {}                         # A row of data separated into elements of a dictionary
lstTable = []                       # A dictionary that acts as a 'table' of rows
strMenu = ""                        # A menu of user options
strChoice = ""                      # A Capture the user option selection

#-- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

objFile = open("ToDoList.txt", "r")

for row in objFile:
    strData=row.split(',') #Returns a list!
    dicRow = {'Task':strData[0], 'Priority': strData[1]}
    lstTable.append(dicRow)
objFile.close()

# # -- Input/Output -- #
# # Step 2 - Display a menu of choices to the user
while True:
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

#     # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable:
            print("Your list is empty")
        else:
            print("Your current list is: \n Task  Priority")
            for row in lstTable:
                print(row["Task"]+ "," + row["Priority"])
        continue
#
#
#     # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
            strTask=str(input("Enter your to do item:\n"))
            strPrio=str(input("Enter your priority value:\n"))
            dicRow = {"Task": strTask, "Priority": strPrio}
            lstTable.append(dicRow)
            print(f'{strTask.title()} has been added to your to do list\n Here is your current list')
            for j in lstTable:
                print(j["Task"] + "," + j["Priority"])

            continue
#
#    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        DelItem=str(input("Your weekend seems to be full\nDo you want to remove the last item? Y/N"))
        if DelItem.lower() =='n':
            print('Alright, we have saved all your to do items')
        elif DelItem.lower() == 'y':
            del lstTable[len(lstTable)-1]
            print('Your last item was deleted')
            print('Here is your current to do items and their respective priority values')
            for row in lstTable:
                print(row["Task"] + "," + row["Priority"])
        continue
#
#     # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile=open('ToDoList.txt','w')
        for row in lstTable:
            objFile.write(row['Task'] + ',' + row['Priority'])
        objFile.close()
        print('Your ToDoList.Txt file is saved')
        continue
#
#     # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting the program')
        break  # and Exit the program


