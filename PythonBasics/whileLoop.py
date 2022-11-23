# mainNumber = 15
# while True:
#     userInput = int(input("Guess a number 0 to 20: "))
#     print(f"You have entered: {userInput}")
#     if userInput == mainNumber:
#         break
#     else:
#         continue
# print("DONE! You have guessed it!")

# another example
capitals = {
    "Peru": "Lima",
    "Philippines": "Manila",
    "Spain": "Madrid",
    "Ethiopia": "Addis Adaba",
    "Ghana": "Accra"
}

userInput = "spain"
for country, capital in capitals.items():
    print("Current country: " + country)
    if userInput.upper() == country.upper():
        print("Capital is: " + capital)
        break
    else:
        continue




