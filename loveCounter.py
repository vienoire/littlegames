print("Welcome to the Love Counter! Enter your name and surname: ")
name1=input()
print("Now your lover's name: ")
name2=input()
name3= name1.lower() + name2.lower()
num1=name3.count("a")+ name3.count("e")+name3.count("k")+ name3.count("h")
num2=name3.count("b")+ name3.count("y")+name3.count("i")+ name3.count("k")
print(f'Chances of a happy living calculated: {num1*10+num2}½')
