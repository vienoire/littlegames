import random

print('''            U _____ u  _        ____   U  ___ u  __  __  U _____ u 
 __        __\| ___"|/ |"|    U /"___|   \/"_ \/U|' \/ '|u\| ___"|/ 
 \"\      /"/ |  _|" U | | u  \| | u     | | | |\| |\/| |/ |  _|"   
 /\ \ /\ / /\ | |___  \| |/__  | |/__.-,_| |_| | | |  | |  | |___   
U  \ V  V /  U|_____|  |_____|  \____|\_)-\___/  |_|  |_|  |_____|  
.-,_\ /\ /_,-.<<   >>  //  \\  _// \\      \\   <<,-,,-.   <<   >>  
 \_)-'  '-(_/(__) (__)(_")("_)(__)(__)    (__)   (./  \.) (__) (__)''')

level = input("You must try to guess the number I chose in between 1-100. Choose a level: hard or easy? ")

def numgame(level):
    number = random.randint(1, 100)
    #print(f"ba ba--{number}")
    hm = 0
    isdone = False
    
    if level == "easy":
        chance = 10
    else:
        chance = 5
    
    while chance != 0 and not isdone:
        num1 = int(input(f"Make a guess.\nYou have {chance} chances left. "))
        
        if num1 == number:
            print("Congratulations! You got it!")
            hm = 1
            isdone = True
        else:
            chance -= 1
            if num1 < number:
                print("Too low!")
            else:
                print("Too high!")

    if hm == 0:
        print('''\  \///  _ \/ \ /\  / \   /  _ \/ ___\/__ __\
 \  / | / \|| | ||  | |   | / \||    \  / \  
 / /  | \_/|| \_/|  | |_/\| \_/|\___ |  | |  
/_/   \____/\____/  \____/\____/\____/  \_/  ''')
        print(f"The number was {number}.")

numgame(level)
