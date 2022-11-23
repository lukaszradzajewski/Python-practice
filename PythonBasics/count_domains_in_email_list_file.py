"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""
# my solution
# input_file = "./SampleFiles/randomEmailsV2.csv"
# output_file = "./SampleFiles/emailDomainCount.json"
# domainCount = {}
# domainList = []
# with open(input_file, "r") as f:
#     emails = f.read()
#     emailList = emails.split(",")
#     for i in emailList:
#         email = i.partition("@")
#         domainList.append(email[2])
#         for j in range(len(domainList)):
#             domainCount[domainList[j]] = domainList.count(domainList[j])
#
# print(domainList)
# print(domainCount)
# f.close()
#
# with open(output_file, "w") as f:
#     f.write(str(domainCount))
#
# f.close()


# udemy solution

import json

input_file = "./SampleFiles/count_domains_in_email_list_file_exercise_input.csv"
output_file = "./SampleFiles/count_domains_in_email_list_file_exercise_output.json"


def get_emails_from_file(file_path):
    with open(file_path, "r") as f:
        emails_raw = f.readlines()

    emails_clean = [i.strip(',\n') for i in emails_raw]

    return emails_clean


def count_domains_option_1(list_of_emails):
    # Solution option 1
    email_counts = dict()
    for email in list_of_emails:
        domain = email.split('@')[-1]
        if domain not in email_counts.keys():
            email_counts[domain] = 1
        else:
            email_counts[domain] = email_counts[domain] + 1

    return email_counts


def count_domains_option_2(list_of_emails):
    domains_list = []
    for email in list_of_emails:
        domain = email.split('@')[-1]
        domains_list.append(domain)

    unique_domains = set(domains_list)

    email_count = dict()
    for domain in unique_domains:
        email_count[domain] = domains_list.count(domain)

    return email_count


def save_output_in_json_file(counts_dict, json_file_path):
    with open(json_file_path, "w") as f:
        json_obj = json.dumps(counts_dict)
        f.write(json_obj)


emails_list = get_emails_from_file(input_file)

# Solution Option 1
# count1 = count_domains_option_1(emails_list)
# print(count1)

# Solution Option 2
count2 = count_domains_option_2(emails_list)
save_output_in_json_file(count2, output_file)
print(count2)
