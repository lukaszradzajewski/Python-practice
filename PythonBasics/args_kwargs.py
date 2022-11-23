def addition(*args):
    return sum(args)


print(addition(2, 4, 6, 8))


def food(**kwargs):
    for item in kwargs:
        print(f"{kwargs[item]} is a {item}")


food(fruit='cherry', vegetable='potato', boy='lucas')


def animals(**kwargs):
    for item in kwargs:
        print(f"{kwargs[item]} is a {item}")


animal_dict = {'dog': 'Kama', 'cat': 'bajka'}
animals(**animal_dict)
