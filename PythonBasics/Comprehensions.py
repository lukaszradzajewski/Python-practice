

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
x = {char: sentence.count(char) for char in set(sentence)}
print(set(sentence))
print(x)


# inline condition
y = True if 1 > 0 else False
print(y)

# Zip

names = ['tim', 'joe', 'billy', 'sally']
ages = [21, 19, 18, 43]
eye_color = ['blue', 'brown', 'brown', 'green']

print(list(zip(names, ages, eye_color)))