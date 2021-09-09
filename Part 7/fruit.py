fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green, citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

veg.update(fruit)
print(veg)

print()

shell_name = fruit.copy()
shell_name.update(veg)
print(shell_name)
print(veg)
print(fruit)