import random
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
lime = "\033[92m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# Bold colours
blackb = "\033[1;30m"
redb = "\033[1;31m"
greenb = "\033[1;32m"
limeb = "\033[1;92m"
yellowb = "\033[1;33m"
blueb = "\033[1;34m"
magentab = "\033[1;35m"
cyanb = "\033[1;36m"
whiteb = "\033[1;37m"

# Reset formatting
reset = "\033[0m"

"""map = [[],[],[],[],[],[]]
map[0].append("    ")
for i in range(len(map)):
    for seat in range:
        print()
        """

board = ["""
["     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36"],
["                                                                                                                "],
["1    0  0  0  0  0  0                          0  0  0  0  0  0  0  0                          0  0  0  0  0  0 "], #36 x (1-1)
["                                                                                                                "],
["2    0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0 "], #36 x (2-1)
["                                                                                                                "],
["3    0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0 "], #36 x (3-1)
["                                                                                                                "],
["4    0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0 "], #36 x (4-1)
["                                                                                                                "],
["5    0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0 "], #36 x (5-1)
["                                                                                                                "],
["6    0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0  0  0  0  0              0  0  0  0  0  0  0  0 "], #36 x (6-1)
["                                                                                                                "],
["7          0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0       "]  #36 x (7-1)
"""]
seatrow = -1
def board(cinema,seatrow):
    global reset
    print("     ", end= "")
    for length in range(len(cinema[0])):
        print(length + 1, end = (" " * (3 - (len(str(length + 1))))))
    print()
    print()
    for row in range(len(cinema)):
        if seatrow == row + 1: # if selected row, set red
            global limeb
            print(limeb, end = "")
        print(f"{row+1}    ",end= "") # print row number
        for column in range(len(cinema[0])): # printing each seat in the row
            if cinema[row][column] == "X": # if it is X, set cyan
                global cyanb
                print(cyanb, end = "")
                print(f"{cinema[row][column]}", end= "  ")
                if seatrow == row + 1:
                    print(limeb, end = "") # set back to red if selected
                else: 
                    print(reset, end = "") # revert to default if not selected
            elif cinema[row][column] == "#":
                global magentab
                print(magentab, end = "")
                print(f"{cinema[row][column]}", end= "  ")
                if seatrow == row + 1:
                    print(limeb, end = "") # set back to red if selected
                else: 
                    print(reset, end = "")
            elif cinema[row][column] == "": # if empty print space
                print(" ", end= "  ")
            else:
                print(f"{cinema[row][column]}", end= "  ") # if not X or empty, print (0)
        
        print(reset) # set colour to default
        print()
    if totaltickets - i != 0:
       print(f"You have {totaltickets - i} seat/s left to choose")
    else:
        print()
        
def screenwipe():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

cinema = [["0","0","0","0","0","0","","","","","","","","","0","0","0","0","0","0","0","0","","","","","","","","","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0","0","0","0","0","","","","","0","0","0","0","0","0","0","0"],["","","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","",""]]
zeros = sum(row.count("0") for row in cinema)

for i in range(random.randint(0,zeros)):
    ranrow = -1
    rancolumn = -1
    count = 0
    while cinema[ranrow][rancolumn] == "" or cinema[ranrow][rancolumn] == "#" or (ranrow == -1 and rancolumn == -1):
        ranrow = random.randint(0,len(cinema)-1)
        rancolumn = random.randint(0,len(cinema[0])-1)

        
    cinema[ranrow][rancolumn] = "#"
zeros = sum(row.count("0") for row in cinema)
print()
print("Welcome to the cinema")

if zeros == 0:
    print("The cinema is fully booked, please book for a different movie")
    exit()
adult = zeros + 1
child = zeros + 1
totaltickets = adult + child
while totaltickets > zeros:
    print(f"available seats: {zeros}")
    adult = int(input(f"How many adult tickets would you like to purchase? : "))
    screenwipe()
    totaltickets = 0 + adult
    if totaltickets > zeros:
        screenwipe()
        
        print(f"Sorry, there is/are only {zeros} seat/s remaining, please book again.")
        continue
    print(f"available seats: {zeros - totaltickets}")
    child = int(input("How many child tickets would you like to purchase? : "))
    totaltickets = totaltickets + child
    if totaltickets > zeros:
        screenwipe()
        print(f"Sorry, there is/are only {zeros} seat/s remaining, please book again.")
        
        continue
screenwipe()
for i in range(totaltickets):
    seatrow = -1
    board(cinema,seatrow)

    seatrow = int(input("Which row would you like to book a seat on?: "))

    seatcolumn = -1
    while cinema[seatrow-1][seatcolumn-1] == "" or seatcolumn == -1 or cinema[seatrow-1][seatcolumn-1] == "X" or cinema[seatrow-1][seatcolumn-1] == "#":
        board(cinema,seatrow)

        if seatcolumn == -1:
            seatcolumn = int(input(f"Which seat in row {seatrow} would you like to book a seat on?: "))
        elif cinema[seatrow-1][seatcolumn-1] == "":
            seatcolumn = int(input(f"Which seat in row {seatrow} would you like to book a seat on? (no seat {seatcolumn} in row {seatrow}): "))
        elif cinema[seatrow-1][seatcolumn-1] == "X" or cinema[seatrow-1][seatcolumn-1] == "#":
            seatcolumn = int(input(f"Which seat in row {seatrow} would you like to book a seat on? (seat {seatcolumn} in row {seatrow} is booked): "))

    cinema[seatrow-1][seatcolumn-1] = "X"  
totaltickets = i 
seatrow = -2
board(cinema,seatrow)
print("These are your selected seats")
price = (child * 9.99) + (adult * 14.99)
print(F"please pay £{price}")
input("Put in card information: ")
print("Thank you for booking with us, enjoy your movie!")
#HERE!!!!!!!!!!!!!!!!!!


