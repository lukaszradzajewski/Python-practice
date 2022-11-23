import pdb

# example 1
# sample_file = "./SampleFiles/programming_language_wikipedia.txt"
#
# with open(sample_file, "r") as f:
#     content = f.read()
#
#
# print(content)

# example 2
countries_file = "./SampleFiles/list_of_countries_with_no_comma.txt"
with open(countries_file, "r") as f:
    # countries = f.read()
    countries = f.readlines()


list_of_c = [i.strip() for i in countries]

pdb.set_trace()

