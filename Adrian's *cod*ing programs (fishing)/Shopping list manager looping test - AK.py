additem = "0"
removeitem = "0"
count = 0
itemsadded = []
itemsremoved = []

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
    for i in range(len(list)):
        if i == (len(list) - 2):
            print(f"{list[i]} and ", end="")
        elif i == (len(list) - 1):
            print(f"{list[i]} ", end="")
        else:
            print(f"{list[i]}, ", end="")
       




shoppinglist = []

option = 0
message = ""
while option != "6":

    addorrem = False
    menu = True
            
    print()
    printmenu(menu)
    if count > 1 and prevadd == True:
        createlist(itemsadded)
        print ("were added to your shopping list.")
    if count > 1 and prevrem == True:
        createlist(itemsadded)
        print("were removed from your shopping list.")
    else:
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
            printlist()
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
                else:
                    shoppinglist.append(additem)
                    if s(additem) == False:
                        message =(f"{additem} was added to your shopping list.")
                    else:
                        message =(f"{additem} were added to your shopping list.")
                    itemsadded.append(additem)
    

                
                    

    if option == "2":
        count = 0
        itemsremoved = []
        prevrem == True
        addorrem = True
        while removeitem != "":
            printlist()
            removeitem = input("What item would you like to remove?: ")
            removeitem = normalize(removeitem) 
            count = count + 1
            if removeitem != "":

                if removeitem[-1] == "." and (removeitem[0:(len(removeitem)-1)]).isnumeric():
                    if (int(removeitem[0:(len(removeitem)-1)]) <= len(shoppinglist)) and int(removeitem[0:(len(removeitem)-1)]) > 0 :
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
                else:
                    if s(removeitem) == False:
                        message = (f"{removeitem} is not on your shopping list.")
                    else:
                        message = (f"{removeitem} are not on your shopping list.")

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



