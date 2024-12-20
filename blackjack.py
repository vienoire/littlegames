import random

print('''==================================================
    ____  _            _       _            _    
   | __ )| | __ _  ___| | __  | | __ _  ___| | __
   |  _ \| |/ _` |/ __| |/ /  | |/ _` |/ __| |/ /
   | |_) | | (_| | (__|   <   | | (_| | (__|   < 
   |____/|_|\__,_|\___|_|\_\  |_|\__,_|\___|_|\_\
                                                 
==================================================
                ♠ ♥ ♦ ♣ BLACKJACK ♠ ♥ ♦ ♣
==================================================
   • Dealer vs Player! 
   • Get as close to 21 without going over.
   • Aces can be 1 or 11. Face cards are worth 10.
   .Two Aces make you lose
==================================================
''')

while True:
    pickcard = input("Do you want to play? Please enter y or n: ").lower()
    if pickcard == "y":
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A"]
        dealer = [random.choice(cards), random.choice(cards)]
        dealorg = dealer.copy()

        def agame(list):
            if list[0] == "A" and list[1] == "A":
                list[0] = 1
                list[1] = 11
                anum = 2
            elif list[0] == "A":
                if list[1] + 11 > 21:
                    list[0] = 1
                else:
                    list[0] = 11
                anum = 1
            elif list[1] == "A":
                if list[0] + 11 > 21:
                    list[1] = 1
                else:
                    list[1] = 11
                anum = 1
            else:
                anum = 0
            total = list[0] + list[1]
            return total, anum


        deal = agame(dealer)[0]
        i = 2
        while deal < 17:
                dealer.append(random.choice(cards))
                dealorg = dealer.copy()
                if dealer[i] == "A":
                    if deal + 11 > 21:
                        dealer[i] = 1
                    else:
                        dealer[i] = 11
                deal += dealer[i]
                i += 1
        user = [random.choice(cards), random.choice(cards)]
        userback = user.copy()
        numa = agame(user)[1]
        score = agame(user)[0]
        a = 2
        while True:
            print(f"Your Cards: {userback}, current score: {score}\nDealer's first card: {dealorg[0]}\n")
            another = input("Do you want to take another card? y or n: ").lower()

            while another not in ["y", "n"]:
                print("Invalid input. Please enter y or n.")
                another = input("Do you want to take another card? y or n: ").lower()

            if another == "y":
                user.append(random.choice(cards))
                userback = user.copy()
                if user[a] == "A":
                    numa += 1
                    if numa == 3:
                        score = 23
                    elif numa == 2:
                        if user[0] == "A":
                            score = 22 + user[1]
                        elif user[1] == "A":
                            score = 22 + user[0]
                        else:
                            score = user[0] + user[1] + 22
                    else:
                        if score  + 11 > 21:
                            user[a] = 1
                        else:
                            user[a] = 11
                        score += user[a]
                else:
                    score += user[a]
                a += 1

            if another == "n" or score > 21:
                if score < 22 and deal < 22:
                    if score > deal:
                        print(f"Congrats, you won!🥳\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                    elif score == deal:
                        if (dealorg == ["A", 10] or dealorg == [10, "A"]) and (userback == ["A", 10] or userback == [10, "A"]):
                            print(f"What are the chances! You both got a Blackjack, it's a push.\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                        elif dealorg == ["A", 10] or dealorg == [10, "A"]:
                            print(f"You Lost. Dealer got a Blackjack.😔\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                        elif userback == ["A", 10] or userback == [10, "A"]:
                            print(f"You won with a Blackjack!🥳\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                        else:
                            print(f"It's a push, noone wins!\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                    else:
                        print(f"You Lost!😔\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")

                elif score > 21 and deal > 21:
                    print(f"You both busted: You Lose.😔\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")

                elif score > 21:
                    print(f"You busted and Lost.😔\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                else:
                    print(f"Congrats, you won!🥳\nYour Cards: {userback}, Your Score: {score}\nDealer's Cards: {dealorg}, score: {deal}.")
                break

    elif pickcard == "n":
        break
    else:
        print("Please enter y or n next time. ")
