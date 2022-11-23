import random

myNumber = random.randint(100, 200)
print(myNumber)

myNumber2 = random.randrange(10)
print(myNumber2)

# example: random list
# myList = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# random.shuffle(myList)
# print(myList)

# example: pick a random element from a list
myList = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(random.choice(myList))

# example: pick a few random elements from a list
print(random.sample(myList, 3))





