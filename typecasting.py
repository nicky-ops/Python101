age = input ("what is your age? ")

data_type = type(age)

age = int(age)
print(age*9)

grocery_list = ["Onions", "Tomatoes", "Brocolli", "Garlic", "Onions", "Onions"]
print(type(grocery_list))

grocery_list = tuple(grocery_list)
print(type(grocery_list))
print(grocery_list)

grocery_list = set(grocery_list)
print(type(grocery_list))
print(grocery_list)