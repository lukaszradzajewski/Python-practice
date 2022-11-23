# a = 11
# b = 5
# c = 30
# d = 10
#
# if a < b:
#     print("'a' is less than 'b'")
# elif a > b:
#     print("'a' is greater than 'b'")
# else:
#     print("N/A")

############
shows = ["Friends", "The Office", "Breaking Bad", "Stranger Things"]
movies = ["Rocky", "Jaws", "Batman", "Wonder Woman"]

my_choice = "The Office"
if my_choice in shows:
    print("Your choice is a show.")
elif my_choice in movies:
    print("Your choice is a movie.")
else:
    print("Your choice is unknown.")

#############
theater = "XYZ"
ageLimit = 17

print(f"Welcome to {theater} theaters!")

userInput = int(input("Enter your age: "))
print(f"User input is {userInput}")

if userInput >= ageLimit:
    print("Enjoy the movie")
else:
    adult = input("Is another adult with you? yes or no: ")
    if adult == "yes":
        print("Enjoy the movie")
    else:
        print(f"You must be {ageLimit} years old to watch this movie.")



