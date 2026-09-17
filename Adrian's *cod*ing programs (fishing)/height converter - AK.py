name= input("what is your name?: ")
height = float(input("Enter your height in cm: "))
print(f"Hi {name}!")
meters = height/100
inches = height/2.54
print(f"Your height is {meters} m.")
print(f"That is {round(inches, 2)} inches.")
print(f"Taller than 180 cm: {180<height}")