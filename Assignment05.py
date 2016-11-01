'''
Create a script that manages a ToDo list
    Data contains two columns, Task and Priority
        Stored as dictionary values
        + Read the list to the User
    Data is combined into a list to create a table of data
    Provide User with option to add/remove data from list
        and save on exit
'''


File = open("ToDo.txt", "r")
Headers = ["Task", "Priority"]
dtable = []
while True:
    # read ToDo.txt
    # display content of ToDo to User
    for LN in File:
        x = LN.split(",")
        current = {Headers[0]: x[0], Headers[1]: x[1].strip("\n")}
        dtable.append(current)
    break

while True:
#display options to User
    print("Current Priorities:")
    #print(dtable)
    for each in dtable:
        print(each)
    print("--------------------------------------")
    print("Choose 1 to Add task")
    print("Choose 2 to Remove task")
    print("Choose 3 to Save new tasks to ToDo.txt and Exit")
    print("--------------------------------------")
    choice = int(input("Choose an option: (1/2/3)" + "\n"))

#add new data
#get inputs
    if choice == 1:
        T = input("Enter Task: ")
        P = input("Enter Priority: ")
        #create data as dictionary
        nList = {Headers[0]: T, Headers[1]: P}
        #append dictionary to list
        dtable.append(nList)

#delete data
#choose data to delete
    elif choice == 2:
        try:
            D = int(input("What item in the list should be deleted?" + "\n"))
            dtable.pop(D)
        #when item is not identified in list
        except:
            print("Please enter a valid number")
            break

#save data
    elif choice == 3:
        File.close()
        Save = open("ToDo.txt", "w")
        print("ToDo.txt Updated with new data entries")
        print("Goodbye")
        #read dictionary values by key
        for dict in dtable:
            data = (dict['Task'] +","+ dict['Priority'] + "\n")
            Save.write(data)
        break
        Save.close()

#option not in menu
    else:
        print("Option Unavailable")



