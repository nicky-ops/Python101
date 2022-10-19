
from cgi import print_arguments


can_code = True

if can_code ==  True:
    print("You can code!")
else:
    print("You dont know how to code yet!")


teacher = "Kalob Taulien"

if teacher.lower() == "Kalob Taulien":
    print("Show teacher Portal")
else:
    print("Try again!")


name = input("What is your name? ")
name = name.lower()
if name == "Bob":
    print("Welcome Bob!")
    bring_food = "Pizza"
elif name == "Kalob":
    print("Welcome to your account")
    bring_food = "Tacos"
else:
    print("You're not Bob get outta here!")
    bring_food = "Salmon"

print(f"You are eating {bring_food}")


age = 18;
if age >= 18:
    print("Proceed to the next booth")