items = ["one","Two","Three","Four", "Five", "Six"]

# for item in items:
#     if item == "Two" or item == "Four":
#         continue
#     print(item)

# for item in items:
#     if item == "Three":
#         break
#     print(item)

num = 0
while num <= 39:
    num = num +1
    if num % 2 == 0:
        continue
    print(num)

count = 0
while count <= 1_000_000:
    count = count + 1
    if count == 13:
        break
    print(count)