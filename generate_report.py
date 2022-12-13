#!/usr/bin/env python3
import csv
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

def read_employees(csv_file_location):
    employee_list = []
    departments = {}
    with open(csv_file_location, newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect = 'empDialect' )
        for data in reader:
            employee_list.append(data)
        # for row in reader:
        #     # print(row[' Development'])
        #     if row["Development"] in departments:
        #         departments[row["Development"]] +=1
        #     if row["Development"] not in departments:
        #         departments[row["Development"]] = 1 
    return employee_list

print(read_employees('employ.csv'))
# csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
# employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')