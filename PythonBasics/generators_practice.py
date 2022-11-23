# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# y = map(lambda i: i ** 2, x)
#
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
#
# print("For Loop Starts")
# for i in y:
#     print(i)


# generators

def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)

filepath = '../SampleFiles/convertcsv.csv'


def csv_reader(filename):
    for row in open(filename):
        if row.__contains__("Hamilton"):
            yield row


hamilton_row = csv_reader(filepath)
print(*hamilton_row)
