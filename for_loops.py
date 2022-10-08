fav_foods = ["Pizza", "Tacos", "Salmon"]

for food in fav_foods:
    print(f"My favourite food is {food}")
    for letter in food:
        print(letter)


# Iterating a Dictionary

details = {
    "name":"Nickson",
    "twitter":"@nickyrutto",
    "instagram": "@coding.for.everyone"
}
for key, value in details.items():
    print(f"The key is {key} and the value is {value}")