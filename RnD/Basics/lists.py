fruits = ['apples', 'bananas', 'grapes', 'oranges', 'pears']

print(fruits[1])
print(fruits[1:4])

fruits[2] = "kiwi"
fruits.append("cherries")
fruits.insert(2, "peaches")

print(fruits)

fruits.remove("kiwi")

print(fruits.sort())

print(fruits.reverse())

fruit_length = len(fruits)
print(fruit_length)

vegetables = ['carrots', 'peas', 'onions']
produce = fruits + vegetables
print(produce)
