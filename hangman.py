import random
animals = ["panda", "lion", "elephant", "giraffe", "tiger", "kangaroo", "koala", "zebra", "cheetah", "rhino",
           "hippopotamus", "monkey", "gorilla", "bear", "wolf", "fox", "deer", "rabbit", "squirrel", "penguin", "owl"]

fruits = ["apple", "banana", "orange", "grape", "pineapple", "mango", "strawberry", "blueberry", "kiwi", "peach",
          "pear", "plum", "watermelon", "cherry", "apricot", "papaya", "melon", "lemon", "fig", "nectarine", "nectar"]

states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida",
          "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
          "maryland", "massachusetts"]
category=input("Please choose a category: animal, fruit, state.")
if category=="animal":
    word = animals[random.randint(0, 20)]
elif category=="fruit":
    word = fruits[random.randint(0, 20)]
else:
    word = states[random.randint(0, 20)]

lives=len(word)-1
guess = ["_"] * len(word)
lastcall=""
def known(letter):
    a=int(0)
    for i in word:
        if i == letter:
            guess[a]=letter
        else:
            pass
        a+=1
    guestr=""
    for i in guess:
        guestr+=i
    return guestr

answ= input((f"Welcome to the Hangman game! Here is your {category} to guess!"))
while lives!=0 and lastcall!=word:
    if answ in word:
        print(f"Congrats! {known(answ)}")
        lastcall=known(answ)
    else:
        print(f"Ah-oh. Don't let your man die. {known(answ)}")
        lives-=1
    if lastcall!=word:
        answ=input("Guess again: ")

if lastcall==word:
    print(f"Congrats! You've guessed the word: {word}")
else:
    print(f"Game over. You've run out of lives. Your word was {word}")