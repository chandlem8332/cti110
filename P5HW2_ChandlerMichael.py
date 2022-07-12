# Math Quiz
# July 12th 2022
# CTI-110 P5HW2 - Math Quiz
# Michael Kord Chandler
#



def main():
    menu()

def menu():
    print("Welcome to Math Quiz")
    repeat = 1
    while repeat != 0:
        print()
        print()
        print("MAIN MENU")
        print("------------------------------")
        #print("-"*30)
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()

        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            print("Add Number")
            addNumbers()
        elif choice == '2':
            print("Subract Numbers")
            subNumbers()
        elif choice == '3':
            repeat = 0
        else:
            print("Not a valid entry.")
            print("Try again.")
            repeat = 1
    print("Thank you for playing...")
    print("Bye!!")

def addNumbers():
    count = 1
    import random
    num1 = (random.randint(1,11))
    num2 = (random.randint(1,11))
    print(num1)
    print("+",num2)
    answer = num1 + num2
    user_input = int(input("Enter answer. \n"))
    while user_input != answer:
        if user_input < answer:
            print("Sorry, guess is too low. \n")
            count += 1
        else:
            print("Sorry, guess is too high. \n")
            count += 1
        user_input = int(input("Try again: "))
    print("Congratulations!!!! You answer is correct.")
    print("Number of guesses:",count)

def subNumbers():
    count = 1
    import random
    num1 = (random.randint(1,11))
    num2 = (random.randint(1,11))
    print(num1)
    print("-",num2)
    answer = num1 - num2
    user_input = int(input("Enter answer. \n"))
    while user_input != answer:
        if user_input < answer:
            print("Sorry, guess is too low. \n")
            count += 1
        else:
            print("Sorry, guess is too high. \n")
            count += 1
        user_input = int(input("Try again: "))
    print("Congratulations!!!! You answer is correct.")
    print("Number of guesses:",count)

main()
