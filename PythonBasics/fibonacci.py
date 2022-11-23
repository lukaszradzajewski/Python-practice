def fib(x):
    if x == 1:
        return x
    elif x == 0:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


fib_of = 10

if fib_of < 0:
    print("Fibonacci sequence exists only for positive numbers!")
else:
    for i in range(fib_of):
        print(fib(i))

print("-----------------------------")


def fib2(x):
    a, b = 0, 1
    while a < x:
        yield a
        a, b = b, a + b


for i in fib2(10):
    print(i)
