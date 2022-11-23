capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
print(type(capitals))

france_capital = capitals["France"]
print(france_capital)

france_capital2 = capitals.get("France")
print(france_capital2)

# get key that does not exist
poland_capital = capitals.get("Poland")
print(poland_capital)
# returns a None(null) value

# default value for a key
germany_capital = capitals.get("Germany", "NOT EXIST!")
print(germany_capital)

# Adding item to dictionary
capitals["Kenya"] = "Nairobi"
print(capitals)

capitals.update({"India": "New Delhi"})
print(capitals)

# Adding a key that already exists overrides it
capitals["USA"] = "Washington DC2"
print(capitals)
# default_cap = capitals.setdefault("Poland", "defaultValue")
# print(default_cap)
# print(capitals)

# Creating lists of values and list of keys
all_keys = list(capitals.keys())
all_values = list(capitals.values())
print(all_keys[0])
print(all_values[0])

# Another example of dictionary
employee = {"name": "John Doe",
            "age": 25,
            "phone": 123456789,
            "title": "Sr. Software Engineer",
            "skills": ["AWS", "Python", "Java", "Docker"]
            }

e_skills = employee["skills"]
print(f"Employee has {len(e_skills)} skills")


