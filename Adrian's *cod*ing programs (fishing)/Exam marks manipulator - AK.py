lowestmark = 200
highestmark = -1
total = 0
enter = 0
mark = int(input("Enter a mark (or -1 to finnish): "))
while mark != -1:
    if (mark < 0 or mark > 100):
        print("Invalid mark - must be 0 to 100.")
        continue
    enter = enter + 1
    total = total + mark
    if mark > highestmark:
        highestmark = mark
    if mark < lowestmark:
        lowestmark = mark
    mark = int(input("Enter a mark (or -1 to finnish): "))
if enter == 0:
    average = 0
    highestmark = 0
    lowestmark = 0

else:
    average = total/enter
print(f"Marks entered: {enter}")
print(f"Average: {average}")
print(f"Highest: {highestmark}")
print(f"Lowest: {lowestmark}")