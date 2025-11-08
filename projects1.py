# we all have played snake,water gun game in our childhood . if you have not google thr rules of this game and write a python program 
# capable of playing this game with the user.

"""
1 for snake
-1 for water 
0 for you

"""
import random




computer = random.choice([-1, 0, 1])
youstr = input("Enter the choice : ")
youDict = {"s":1, "w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}


you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a drow")

else:
    if(computer == -1 and you == 1 ):
        print("you Win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer == 1 and you == -1):
        print("You lose !")

    elif(computer == 1 and you == 0):
        print("You Win !")

    elif(computer == 0 and you == -1):
        print("You Win !")

    elif(computer == 0 and you == 1):
        print("You lose !")

    else:
        print("Something went wrong !")

    

