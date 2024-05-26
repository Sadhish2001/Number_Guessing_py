import random

lower = int(input("Enter a lower number : "))
upper = int(input("Enter a upper number : "))

x = random.randint(lower, upper)


while(True):
    level = input("\nEnter your level(Easy(e),Medium(m),Hard(h)): ").lower()
    if level == 'e':
        guesses = 10
        break
    elif level == 'm':
        guesses = 7
        break
    elif level == 'h':
        guesses = 5
        break
    else:
        print("Give correct input")
        
print("")

i=guesses
while(i):
    num=int(input("Enter the number: "))
    guesses -= 1
    if num > x:
        print("Number is High")
        print(f"Guesses left: {guesses}")
    elif num < x:
        print("Number is Low")
        print(f"Guesses left: {guesses}")
    else:
        print("Number is guessed")
        break
    if guesses == 0:
        print("YOUlOSTALL YOUR CHANCES!")
        print(f"The Random Number is {x}")
        break
    