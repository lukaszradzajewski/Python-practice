# Example: function to add two numbers

# def add(a, b):
#     return a + b
#
#
# print(add(2, 2))

# example: function to determine if given state has no sales tax

def salesTax(state):
    statesWithNoSalesTax = ['AK', 'DE', 'MT', 'NH', 'OR']

    if state.upper() in statesWithNoSalesTax:
        return True
    else:
        return False


print(salesTax('AK'))


# example : function that will return number of words that have X length, given a string

def get_count_of_small_words(input_string, max_size=3):
    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)
    return len(small_words)


my_joke_1 = "In Python hashtags are used to tell the computer a line is not worth reading. Much like social media."
print(get_count_of_small_words(my_joke_1, 4))


# example : database
def connectToDatabase(host='test.db.com', username='testuser', password='testpass'):
    print(f"Connection to host: {host}")
    print(f"Username: {username}")


connectToDatabase()
