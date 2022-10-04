import time
import random


# function to leave a vacuum of time between paragraphs
def print_pause(paragraph):
    print(paragraph)
    time.sleep(2)


# function to re enter value for wrong inputs
def wrong_choice(rang):
    value = input("plese enter a valid input:\n")
    if value in rang:
        return value
    else:
        wrong_choice(rang)


# function to check if the number is in the selected range
def number_checker(choice, rang):
    if choice in rang:
        return choice
    else:
        choice = int(input("plese enter a valid number:\n"))
        number_checker(choice, rang)


# function to ramdom my choice
def random_choice(rang):
    return random.choice(rang)


# hard level function
def crowed_floor():
    print_pause("This is a crowed floor, there are alot of armed people here.")
    print_pause("I see 6 doors.")
    print_pause("Each door contains armed people behind it, except one.")
    input_num = int(input("choose door from 1 to 6:\n"))
    choice = number_checker(input_num, range(1, 7))
    ram = int(random_choice(range(1, 7)))
    if choice == ram:
        print("hooray, we ran away from them thanks to you ;).")
    else:
        print("OMG, they caught us and tied me with the ropes again :(.")


# easy level function
def empty_floor():
    print_pause("This is a semi-empty floor, there is one armed person here.")
    print_pause("I see 12 doors.")
    print_pause("All doors are empty.")
    print_pause("But one of them contains armed person behind it.")
    input_num = int(input("choose door from 1 to 12:\n"))
    choice = number_checker(input_num, range(1, 13))
    ram = int(random_choice(range(1, 13)))
    if choice == ram:
        print("OMG, they caught us and tied me with the ropes again :(.")
    else:
        print("hooray, we ran away from them thanks to you ;).")


# story functon
def start():
    print_pause("Last night I was kidnapped in front of my house.")
    print_pause("Today I woke up in an abandoned factory tied up with ropes.")
    print_pause("I was able to untie the ropes, can you help me to escape?")
    print_pause("Now there are two stairs.")
    print_pause("The first stair is heading up.")
    print_pause("The second stairs is heading down.")
    input_num = int(input("Press 1 to go upstairs and 2 to go downstairs:\n"))
    choice = number_checker(input_num, range(1, 3))
    ram = int(random_choice([1, 2]))
    if choice == ram:
        crowed_floor()
    else:
        empty_floor()


# regame choice function
def end(regame):
    regame = regame.lower()
    if regame == "y":
        print_pause("Good choice. I will restart the game right now ;).")
        main()
    elif regame == "n":
        print_pause("Thanks for playing. I will miss you :( ,see you soon!")
        exit()
    else:
        regame = wrong_choice(["y", "n", "Y", "N"])
        end(regame)


# the main function
def main():
    start()
    print_pause("GAME OVER\n")
    regame = input("Would you like to play again? (y/n)")
    end(regame)


# call the main function
if __name__ == '__main__':
    main()
