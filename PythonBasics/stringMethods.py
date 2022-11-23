# fullName = "Lucas Radzajewski"
# nameSplit = fullName.split()
# print(fullName)
# print(nameSplit)

ssn = "111-22-3333"
ssnSplit = ssn.split('-')
print(ssn)
print(ssnSplit[2])

fullName = "  Lucas Radzajewski  "
print(fullName)
fullName_clean = fullName.strip()
print(fullName_clean)

print(fullName_clean.upper())

url = "https://www.google.com"
isHome = url.endswith("com")
print(isHome)

info = "This%20is%20url%20encoded"
info_replaced = info.replace("%20", " ")
print(info_replaced)

