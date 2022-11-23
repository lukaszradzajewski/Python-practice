# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print("dont divide by zero!")

# example print the actual error
# try:
#     a = 5 / 0
# except Exception as e:
#     print(f"Error has happened: {e}")

# example with many exceptions
# try:
#     a = 5 / 0
#     b = {'name': 'foo', 'age': 26}
#     x = b['school']
# except KeyError:
#     print("key error")
# except ZeroDivisionError:
#     print("dividing by zero")

# example: Raise an exception
# try:
#     a = 5 / 0
#     print(foo)
# except Exception as e:
#     print(f"Error has happened: {e}")
#     raise Exception("Something went wrong")

# Example: re-raise exception
try:
    a = 5 / 0
    print(foo)
except Exception as e:
    print("Sending notification")
    raise


