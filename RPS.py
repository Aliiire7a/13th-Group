import random
import re  # Vase Split

print("Welcome to My Game \n Here You Have a Chance to Play the Game of Rock-Paper-Scissors With Me"
      "\n Rules Are Simple : \n Rock Smashes Scissors \n Scissors Cut Paper \n Paper Covers Rock "
      "\n\rHope You Enjoy it ! "
      "\n**********************************************")
yourScore = 0
cpuScore = 0

possible_actions = ('rock', 'paper', 'scissors')

rockAction = 'rock'
scissorsAction = 'scissors'
paperAction = 'paper'
winningScore = ''
try:
    winningScore = input("Please Type in a Value for the Winning Score:")
except EOFError as e:
    print(e)
    exit()
else:
    if winningScore.lower() == "quit" or winningScore.lower() == "q":
        print("Thank You for Playing This Game. I Really Enjoyed it !")
        exit()
    while winningScore.isnumeric() is False:
        print("I Need an Integer to Carry on. Please type in an INTEGER Value ")
        try:
            winningScore = input("Please Type in a Value for the Winning Score:")
        except EOFError as e:
            print(e)
            exit()

while cpuScore < int(winningScore) or yourScore < int(winningScore):
    user_action = " "
    computer_action = (random.choice(possible_actions))
    try:
        userAction = input("Please Select Either Rock, Paper or Scissors (or Quit to exit)")
    except EOFError as e:
        print(e)
        exit()
    while userAction == "":  # vase inke Enter Nazane
        print("You Pressed Enter")
        try:
            userAction = input("Please Select Either Rock, Paper or Scissors (or Quit to exit)")
        except EOFError as e:
            print(e)
            exit()

    if userAction.lower() == "q" or userAction.lower() == "quit":
        print("Thank You for Playing This Game. I Really Enjoyed it !")
        exit()

    userAction = re.split("\s|(?<!\d)[,.](?!\d)", userAction.lower())
    user_action = ""



    for i in range(len(userAction)):
        ua = list(userAction[i])

        size1 = min(len(ua), len(scissorsAction))
        size2 = min(len(ua), len(paperAction))
        size3 = min(len(ua), len(rockAction))

        if userAction[i] != "":
            if userAction[i] == scissorsAction[0: size1]:
                user_action = 'scissors'

            elif userAction[i] == paperAction[0: size2]:
                user_action = 'paper'

            elif userAction[i] == rockAction[0: size3]:
                user_action = 'rock'

    if user_action == computer_action:
        print("It's a Tie! Seems Our Choices Are the Same \n I Had {} and Your Choice Was {}".format(
            computer_action, user_action))
        print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))
    elif user_action == 'rock':
        if computer_action == 'paper':
            print("Clap, Clap, I'm The BEST! \n I Had {} and Your Choice Was {}".format(computer_action,
                                                                                        user_action))
            cpuScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))
        else:
            print("What a Lot of Luck, Wish You Wouldn't Do That \n I Had {} and Your Choice Was {}".format(
                computer_action, user_action))
            yourScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))
    elif user_action == 'paper':
        if computer_action == 'scissors':
            print("Clap, Clap, I'm The BEST! \n I Had {} and Your Choice Was {}".format(computer_action,
                                                                                        user_action))
            cpuScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))
        else:
            print("What a Lot of Luck, Wish You Wouldn't Do That \n I Had {} and Your Choice Was {}".format(
                computer_action, user_action))
            yourScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))

    elif user_action == 'scissors':
        if computer_action == 'rock':
            print("Clap, Clap, I'm The BEST! \n I Had {} and Your Choice Was {}".format(computer_action,
                                                                                        user_action))
            cpuScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))
        else:
            print("What a Lot of Luck, Wish You Wouldn't Do That \n I Had {} and Your Choice Was {}".format(
                computer_action, user_action))
            yourScore += 1
            print("Computer Score ={} \n Your Score ={}".format(cpuScore, yourScore))

    if yourScore == int(winningScore):
        print("*" * 40)
        print(":(((, You Win")
        print("*" * 40)
        try:
            rematch = input("Another one? [Yes/No]")
        except EOFError as e:
            print(e)
            exit()
        while rematch.lower() not in ("yes", "no", "y", "n", "ye"):
            try:
                rematch = input("Please Enter Yes or No")
            except EOFError as e:
                print(e)
                exit()
        if rematch.lower() in ("yes", "y", "ye"):
            yourScore = 0
            cpuScore = 0
            try:
                winningScore = input("Please Type in a Value for the Winning Score:")
            except EOFError as e:
                print(e)
                exit()
            if winningScore.lower() == "quit" or winningScore.lower() == "q":
                print("Thank You for Playing This Game. I Really Enjoyed it !")
                exit()
            while winningScore.isnumeric() is False:
                print("I Need an Integer to Carry on. Please type in an INTEGER Value ")
                winningScore = input("Please Type in a Value for the Winning Score:")
            continue

        if rematch == "no" or rematch == "n":
            break




    elif cpuScore == int(winningScore):
        print("*" * 40)
        print("WOOOHOOO, I HAVE WON THE GAME")
        print("*" * 40)
        try :
            rematch = input("Another one? [Yes/No]")
        except EOFError as e:
            print(e)
            exit()
        while rematch.lower() not in ("yes", "no", "y", "n", "ye"):
            try:
                rematch = input("Please Enter Yes or No")
            except EOFError as e:
                print(e)
                exit()
        if rematch.lower() in ("yes", "y", "ye"):
            yourScore = 0
            cpuScore = 0
            try:
                winningScore = input("Please Type in a Value for the Winning Score:")
            except EOFError as e:
                print(e)
                exit()
            if winningScore.lower() == "quit" or winningScore.lower() == "q":
                print("Thank You for Playing This Game. I Really Enjoyed it !")
                exit()
            while winningScore.isnumeric() is False:
                print("I Need an Integer to Carry on. Please type in an INTEGER Value ")
                winningScore = input("Please Type in a Value for the Winning Score:")
            continue

        if rematch == "no" or rematch == "n":
            break