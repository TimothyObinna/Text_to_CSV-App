import csv
import os
import sys

# Open the text file and read its content
with open(os.path.join(sys.path[0], 'Phone_Number_list.txt'), 'r') as file:
    text = file.read()

# Split the text into rows in a list using a delimiter
rows = text.split()

# Open a new CSV file and write the rows to it
with open(os.path.join(sys.path[0],'Phone_Number_list.csv'), 'w', newline= '') as file:
    write_csv = csv.writer(file)
    write_csv.writerow(['Phone Number List:'])
    for row in rows:
        each_row = row.split()
        write_csv.writerow(each_row)

if write_csv:
    print(" ")
    print('The text file has been converted to the csv file, Phone_Number_list.csv, successfully.')
    print(" ")
else:
    print('The text file is not converted to csv file')
