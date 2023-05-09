import csv

# Python program to demonstrate
# writing to CSV
	
# field names
fields = ['Name', 'Dept', 'Course', 'Scores']
	
# data rows of csv file
rows = [ ['Okechukwu', 'BCH', 'BCH302', '90'],
		['Friday', 'MCB', 'BCH302', '92'],
		['Nicholas', 'BCH', 'BCH302', '91'],
		['Saturday', 'MCB', 'BCH302', '85'],
		['Patrick', 'BCH', 'BCH302', '89'],
		['Desmomd', 'MCB', 'BCH302', '74']]

	
# writing to csv file
with open('school_records.csv', 'w', newline = '') as csvfile:
	# creating a csv writer object
	my_csvfile = csv.writer(csvfile)
		
	# writing the fields
	my_csvfile.writerow(fields)
		
	# writing the data rows
	my_csvfile.writerows(rows)
	
#Reading the csv file
with open('school_records.csv', 'r') as my_csvfile:
	read_file = my_csvfile.read()
	print(read_file)
