import pdb

sample_file = "./SampleFiles/programming_language_wikipedia.txt"
# demo 1
# my_file = open(sample_file, "r")
# content = my_file.read()
# my_file.close()
# pdb.set_trace()

# demo 2
# my_file = open(sample_file, "r")
# content = my_file.readlines()
# my_file.close()
#
# print(content)

# gotcha !!! example of reading twice from the same file
# the .seek()
my_file = open(sample_file, "r")
content = my_file.read()
print(content)
my_file.seek(0)
print("----------")
content2 = my_file.read()
print(content2)
print("2---------")
my_file.close()




