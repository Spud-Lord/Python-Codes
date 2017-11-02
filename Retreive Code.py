#Jake Eaton

import csv
import sys

uid = input('Enter number to find\n')
csv_file = csv.reader(open('students.csv', "r"), delimiter=",")
for row in csv_file:
    if uid == row[9]:
         print(row)
