year = int(input("Please enter a year: "))
if year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a leap year.")
    leap = "yes"
else:
    print(f"{year} is not a leap year.")
    leap = "no"
day = int(input("Please enter a month number (1-12): "))
if day < 0 or day > 12:
    print("no.")
if day == 4 or day == 6 or day == 9 or day == 11:
    print(f"Month {day} of {year} has 30 days.")
if day == 2:
    if leap == "yes":
        print(f"Month {day} of {year} has 29 days.")
    else:
        print(f"Month {day} of {year} has 28 days.")
else:
    print(f"Month {day} of {year} has 31 days.")