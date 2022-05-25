#PyBoss

import csv
from hashlib import new

from sklearn.utils import column_or_1d
#from operator import index #?

#variables
complete_data = []
id = []
name = []
dob = []
ssn = []
state = []

#open Resources/employee_data.csv
csv_path = ('Resources/employee_data.csv')
with open(csv_path) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    #skipping header
    csv_header = next(csv_reader)

  
    for line in csv_reader:
        #adding a new variable which will need more cols later
        complete_data = line
        
        #save into columns - alter stuff
        #origcolumn1 - stays the same - may nor even need
        id = complete_data[0]
        
        #origcolumn2 - divides into two cols
        name = complete_data[1]
        name = name.split()
        first_name = name[0]
        last_name = name[1]

        #origcolumn3 - will b altered
        dob = complete_data[2]

        #origcolumn4 - will b altered
        ssn = complete_data[3]

        #origcolumn5 - State
        state = complete_data[4]
        

        #can use to add new col - will just need one
        complete_data.append(state)

       

        #save back overwritting columns, samples
        for x in complete_data:
           complete_data[1] = first_name
           complete_data[2] = last_name
        print(complete_data)





'''
#output to Analysis/employee_data.csv
file_path = ('Analysis/employee_data.csv')
with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

will loop
    #write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    #write the second row
    csvwriter.writerow(['214', 'Sarah', 'Simpson', '12/04/1985', '***-**-8166', 'FL'])


'''
#converting output to a list to be written to a text file
#file_output = dict.values(output_lines)