# EXAMPLE 1
def someone(name, food = "Pizza"):
    if name.lower() == "nickson":
        print(f"Welcome {name}")
    print(f"Hello {name}. Let's eat some {food}")

someone("Nickson", food= "Oranges")

# DRY - Do not repeat yourself

# EXAMPLE 2
def person(name =None, food = "Milk"):
    if name is None:
        name = "Gully"
    print(f"My name is {name}, and I love {food}")
person()

# EXAMPLE 3
def animal(name =None, food = "Milk"):
    if name is None:
        name = "Gully"
    person_type = "human"
    if name == "Gully":
        person_type = "Cat"
    print(person_type)

    print(f"My name is {name}, and I love {food}")
animal()

# Example 4 Storing a function in a Variable
def calculator (num1, num2):
    total = num1 ** num2
    return total


number = calculator(45, 3)
print(number)