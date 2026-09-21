number = int(input("Enter a 3-digit number: "))
hundred = number // 100
ten = (number % 100) // 10
one = number % 10
print(f"Hundreds: {hundred}")
print(f"Tens: {ten}")
print(f"Units: {one}")
sumofdigits= hundred + ten + one
print(f"Sum of digits: {sumofdigits}")
reversednum = (one*100) + (ten*10) + (hundred)
print(f"Reversed: {reversednum}")
print(f"Even number: {number%2==0}")
