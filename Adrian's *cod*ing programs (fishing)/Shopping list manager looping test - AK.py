
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
def printmenu(menu):
    print("""--- Shopping List ---
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



shoppinglist = []

option = 0
message = ""
while option != "6":
    menu = True
    if option == "3" or option == "5":
            printlist()
            print()
            input("Enter when you would like to return to the menu: ")
    print()
    printmenu(menu)
    print(message)
    print()
    option = input("What would you like to do?: ")
    print()
    menu = False

    if option == "1":
        printmenu(menu)
        additem = input("What would you like to add to the list?: ")
        additem = normalize(additem)
        if additem[-1] == "." and (additem[0:(len(additem)-1)]).isnumeric():
            message = ("Please don't add index numbers to the shopping list, it's too confusing to list.")
        if additem in shoppinglist:
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

    if option == "2":
        printmenu(menu)
        removeitem = input("What item would you like to remove?: ")
        

        removeitem = normalize(removeitem) 
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
        else:
            if s(removeitem) == False:
                message = (f"{removeitem} is not on your shopping list.")
            else:
                message = (f"{removeitem} are not on your shopping list.")

    if option == "3":
        if len(shoppinglist) == 0:
            message = ("Your shopping list is empty.")
        else:
            message = ""
    if option == "4":
        message = (f"There are {len(shoppinglist)} items on your shopping list.")
    if option == "5":
        shoppinglist.sort()
        message = ("Your list was sorted alphabetically")

print("Goodbye!")



