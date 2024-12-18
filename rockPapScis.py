#out of range not included
print("Choose one: 0 for Rock, 1 for Paper, 2 for Scissors")
import random
x=int(input())
y=random.randint(0,2)
if x==0:
    if y==0:
        a=0
    elif y==1:
        a=1
    else:
        a=2
elif x==1:
    if y==0:
        a=2
    elif y==1:
        a=0
    else:
        a=1
else:
    if y==0:
        a=1
    elif y==1:
        a=2
    else:
        a=0

answer=["it's a draw. try again", "You lost.", "You win. Congrats"]
def game(vr):
    if vr==0:
        print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

    elif vr==1:
        print('''   _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)''')

    else:
        print('''  _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)''')

print(f'You chose:\n')
game(x)
print(f'Computer chose: \n')
game(y)
print(answer[a])
