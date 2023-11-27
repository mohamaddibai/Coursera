import re
import operator
import csv

error_dict = {}
user_dict = {}

with open('syslog.log', 'r') as f:
    for line in f:
        info_match = re.search(r"INFO[\s\w]*", line)
        error_match = re.search(r"ERROR[\s\w]*", line)
        user_match = re.search(r'\(([\w]+)\)$', line)

        if error_match:
            error_match = error_match.group(0).strip()
            if error_match in error_dict:
                error_dict[error_match] += 1
            else:
                error_dict[error_match] = 1

        if info_match or error_match:
            user_match = user_match.group(1).strip() if user_match else None
            if user_match in user_dict:
                if error_match:
                    user_dict[user_match]['ERROR'] += 1
                if info_match:
                    user_dict[user_match]['INFO'] += 1
            else:
                user_dict[user_match] = {'ERROR': 0, 'INFO': 0}
                if info_match:
                    user_dict[user_match]['INFO'] += 1
                if error_match:
                    user_dict[user_match]['ERROR'] += 1

# Sorting error_dict by count in descending order
sorted_error_list = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)

# Specify the file names
csv_error_file = 'error_message.csv'
csv_user_file = 'user_statistics.csv '

# Write the data to the CSV file for error_dict with the specified header
with open(csv_error_file, 'w', newline='') as error_file:
    error_writer = csv.writer(error_file)

    # Write the header
    error_writer.writerow(['Error', 'Count'])

    # Write the data
    error_writer.writerows(sorted_error_list)

print(f"CSV file '{csv_error_file}' has been created.")
print(sorted_error_list)

# Write the data to the CSV file for user_dict with the specified header
with open(csv_user_file, 'w', newline='') as user_file:
    user_writer = csv.writer(user_file)

    # Write the header
    user_writer.writerow(['username', 'INFO', 'ERROR'])

    # Write the data
    for username, counts in user_dict.items():
        user_writer.writerow([username, counts['INFO'], counts['ERROR']])

print(f"CSV file '{csv_user_file}' has been created.")
print(user_dict)
