"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""


list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

import random
import string

letters = string.ascii_lowercase

with open("./SampleFiles/randomEmailsV1.csv", "w") as f:
    for domain in list_of_domains:
        for email in range(20):
            randomString = ''.join(random.choice(letters) for i in range(6))
            f.write(randomString + "@" + domain + ",\n")
            # option 2
            # emails = f"{randomString}@{domain}"
            # emailsFormatted = ',\n'.join(emails)
            # f.write(emailsFormatted)

f.close()


