fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green, citrus fruit"}


# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# # del fruit["orange"]
# print(fruit)
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])
# print(fruit)

print(fruit)
# print("-" * 80, '\n')
# print(fruit.keys())
# print("-" * 80, '\n')
# print(fruit.values())
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["Tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
# order_keys = list(fruit.keys())
# order_keys.sort()
# order_keys = sorted(list(fruit.keys()))
# for f in order_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
#
# for val in fruit.values():
#     print(val)
# print("-" * 40)

# for key in fruit:
#     print(fruit[key])
# print("-" * 40)


# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('_' * 40)

# while True:
#     dict_key = (input("Please enter a fruit: ").casefold())
#     if dict_key == "quit":
#         break
#     if dict_key == "":
#         continue
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     if dict_key != " ":
#         print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #    print("We don't have a " + dict_key)
