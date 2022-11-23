# Collect word with 3 or less characters and put in to a list
quote = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime."
smallWords = []
for i in quote.split():
    if len(i) <= 3:
        smallWords.append(i)
print(smallWords)
print("-----------------------")


# range examples
for i in range(10):
    print(i)


