import random
points = 0

def main():
    
    test = int(input("How many questions would you like to receive?: "))
    for i in range(test):
        first = random.randint(2,12)
        second = random.randint(2,12)
        answer = first * second
        generator(first,second,answer,(i+1))
    result(test)

def result(test):
    
    print(f"You scored {points} out of {test}.")
    

def generator(first,second,answer,loop):
    question = -1
    while question < 0 or question > 144:
        question = int(input(f"{loop}. {first} X {second} = "))
        if question < 0 or question > 144:
            print("This quiz can only have answers between 0 and 144; ")
            print("This is a 12 times tables quiz!")
            
    if question == answer:
        print("Correct!")
        global points
        points = points + 1
    else:
        print(f"Wrong - the answer was {answer}.")
main()