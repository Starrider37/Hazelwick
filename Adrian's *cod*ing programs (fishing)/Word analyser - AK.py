word = input("Enter a word: ")
drow = word[::-1]
print(F"Reversed: {drow}")
print(f"Uppercase: {word.upper()}")
print(f"Length: {len(word)}")
lowerdrow = drow.lower()
print(F"Palindrome: {lowerdrow==word.lower()}")
print(f"First letter character code: {ord(word[0])}")
middlecharacter= round(len(word)/2)
if len(word)/2 == float:
    othermiddlenum = len(word)//2
    othermiddle = word[othermiddlenum]
    mid= middlecharacter+othermiddle
else:
    mid = middlecharacter
print(f"Middle character: {mid}")
