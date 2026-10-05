additem = "0"
removeitem = "0"
count = 0
itemsadded = []
itemsremoved = []
history = [[],[]]
remhistory = []
prevadd = False
prevrem = False
def normalize(word):
    word = word.strip()
    word = word.lower()
    word = word.title()
    return word
def s(word):
    if word[-1] == "s":
        end_s = True
    else:
        end_s = False
    return end_s
def printlist():
    print("--- Shopping list ---")
    for i in range(len(shoppinglist)):
        print(f"{i+1}. {shoppinglist[i]}")
    print()
    if addorrem == True:
        print()
        printmessage(count,prevadd,itemsadded,prevrem,itemsremoved,message)
        print(message)
        print()
def printmenu(menu):
    print("""--- Shopping List menu ---
1 Add an item
2 Remove an item
3 View the list
4 count items
5 Sort list
6 Quit
""")
    if menu == False:
        print("""
""")
def endnumber(word):
    if word == "1":
        ending = "ˢᵗ"
    if word == "2":
        ending = "ⁿᵈ"
    if word == "3":
        ending = "ʳᵈ"
    else:
        ending = "ᵗʰ"
    return ending
def createlist(list):
    message = ""
    for i in range(len(list)):
        if i == (len(list) - 2):
            message = message + (f"{list[i]} and ")
        elif i == (len(list) - 1):
            message = message + (f"{list[i]} ")
        else:
            message = message + (f"{list[i]}, ")
    return message
def printmessage(count,prevadd,itemsadded,prevrem,itemsremoved,message):
    if count > 1 and prevadd == True:
        message = createlist(itemsadded)
        message = message + ("were added to your shopping list.")
        
    elif count > 1 and prevrem == True:
        message = createlist(itemsremoved)
        message = message + ("were removed from your shopping list.")
    return message

    
    



shoppinglist = []

option = 0
message = ""
while option != "6":

    addorrem = False
    menu = True
            
    print()
    printmenu(menu)
    message = printmessage(count,prevadd,itemsadded,prevrem,itemsremoved,message)
    print(message)

    prevrem = False
    prevadd = False
    print()
    option = input("What would you like to do?: ")
    print()
    menu = False

    if option == "1":
        prevadd = True
        itemsadded = []
        count = 0
        addorrem = True
        while additem != "":
            count = count + 1
            print()
            printlist()
            if historycontrol == True and history[1][-1] == "remove":
                additem = history [0][-1]
            else:
            #HERE!!!!!!!!!!!!!!!!!!!!!!
                additem = input(f"{len(shoppinglist) + 1}. ")
            additem = normalize(additem)
            if additem != "":

                if additem[-1] == "." and (additem[0:(len(additem)-1)]).isnumeric():
                    message = ("Please don't add index numbers to the shopping list, it's too confusing to list.")

                elif additem in shoppinglist:
                    if s(additem) == False:
                        message = (f"{additem} is already on your shopping list")
                    else:
                        message =(f"{additem} are already on your shopping list")
                    count = count - 1 
                elif additem == "-1":
                    historycontrol = True
                    additem = ""
                else:
                    shoppinglist.append(additem)
                    if s(additem) == False:
                        message =(f"{additem} was added to your shopping list.")
                    else:
                        message =(f"{additem} were added to your shopping list.")
                    itemsadded.append(additem)
                    history[0].append(additem)
                    history[1].append("add")
        additem = "0"

                
                    

    if option == "2":
        count = 0
        itemsremoved = []
        prevrem = True
        addorrem = True
        while removeitem != "":
            print()
            printlist()
            removeitem = input("What item would you like to remove?: ")
            removeitem = normalize(removeitem) 
            count = count + 1
            if removeitem != "":
                # should have set "removeitem[0:(len(removeitem)-1" as a variable; I wouldn't have to repeat it so many times.
                if removeitem[-1] == "." and (removeitem[0:(len(removeitem)-1)]).isnumeric():
                    if (int(removeitem[0:(len(removeitem)-1)]) <= len(shoppinglist)) and int(removeitem[0:(len(removeitem)-1)]) > 0 :
                        remhistory.append(shoppinglist[(int(removeitem[0:(len(removeitem)-1)]))-1])
                        itemsremoved.append(shoppinglist[(int(removeitem[0:(len(removeitem)-1)]))-1])
                        message = (f"The {removeitem[0:(len(removeitem)-1)]}{endnumber(removeitem[0:(len(removeitem)-1)])} item ({shoppinglist[(int(removeitem[0:(len(removeitem)-1)]))-1]}) was removed from your shopping list.")
                        shoppinglist.remove(shoppinglist[(int(removeitem[0:(len(removeitem)-1)]))-1])
                        
                    else:
                        if removeitem[0] == "-":
                            message = (f"The shopping list can't index negative numbers. ({removeitem[0:(len(removeitem)-1)]} is negative).")
                        else:
                            message = (f"Your shopping list only contains {len(shoppinglist)} items.")



                elif removeitem in shoppinglist:
                    shoppinglist.remove(removeitem)
                    if s(removeitem) == False:
                        message =(f"{removeitem} was removed from your shopping list.")
                    else:
                        message =(f"{removeitem} were removed from your shopping list.")
                    itemsremoved.append(removeitem)
                    history[0].append(removeitem)
                    history[1].append("remove")
                else:
                    if s(removeitem) == False:
                        message = (f"{removeitem} is not on your shopping list.")
                    else:
                        message = (f"{removeitem} are not on your shopping list.")
        removeitem = "0"

    if option == "3":
        if len(shoppinglist) == 0:
            message = ("Your shopping list is empty.")
        else:
            message = message = (f"There are {len(shoppinglist)} items on your shopping list.")
            printlist()
            input("Enter when you would like to return to the menu: ")
    if option == "4":
        message = (f"There are {len(shoppinglist)} items on your shopping list.")
    if option == "5":
        if len(shoppinglist) == 0:
            message = ("There are no items in the list to sort.")
        else:
            shoppinglist.sort()
            message = ("Your list was sorted alphabetically")
            printlist()
            input("Enter when you would like to return to the menu")

print("Goodbye!")



