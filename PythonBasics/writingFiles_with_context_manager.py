import pdb

my_string = "I love to program in Python language"

# example 1
# with open("./SampleFiles/sample_output2.txt", "w") as f:
#     f.write(my_string)


# example 2
# my_list = ["user1", "user2", "user3"]
# with open("./SampleFiles/sample_output2.txt", "w") as f:
#     for i in my_list:
#         f.write(str(i + "\n"))

# example 3 (appending)
# var2 = "Also love testing"
# with open("./SampleFiles/sample_output2.txt", "a") as f:
#     f.write("\n" + var2)


# example 4 (join)
languages = ["Python", "JS", "PHP", "Java", "Ruby"]
with open("./SampleFiles/my_fav_languages.csv", "w") as f:
    str_languages = "\n".join(languages)
    f.write(str_languages)



