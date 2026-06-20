import random as re 
print("====================================")
print("welcome to the Dice Simulator Game..")
print("====================================")

while True :
    input("Press Enter to Roll the Dice ....")
    print("Rolling Dice...")

    res = re.randint(1,6)
    print("Result :", res)

    choice = input("Roll Again? (y/n): ").lower()
    if choice !='y':
        print("Game Over!!")
        exit()