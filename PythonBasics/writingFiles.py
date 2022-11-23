import pdb

my_string = "I love to program in Python language"

# example 1

f = open("./SampleFiles/sample_output1.txt", "w")
f.write(my_string)
f.write("\n")
f.write(my_string)
f.close()

