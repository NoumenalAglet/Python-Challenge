#PyBoss

import csv
#so we can use the state abbreviations dict
from us_state_abbrev import us_state_abbrev
import os

#variables
complete_data = [] #could change name to local data or data
id = []
name = []
dob = []
ssn = []
state = []


#open Resources/employee_data.csv
csv_path = os.path.join("Resources", "employee_data.csv")
with open(csv_path) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    #skipping header
    csv_header = next(csv_reader)

  
    for line in csv_reader:
        #adding a new variable which will need more cols later
        complete_data = line
        
        #storing each column as a list and altering as need
        #origcolumn1 - stays the same - may nor even need
        id = complete_data[0]
        
        #splitting name then storing in different variables
        #origcolumn2 - divides into two cols
        name = complete_data[1]
        name = name.split()
        first_name = name[0]
        last_name = name[1]

        #converting date from YYYY-MM-DD to MM/DD/YYYY
        dob = complete_data[2]
        #sperating by '-'
        dob = dob.split('-')
        year = dob[0]
        day = dob[1]
        month = dob[2]
        #putting the pieces back together in new order with a '/'
        dob[0] = day
        dob[1] = month
        dob[2] = year       
        dob = '/'.join([str(item) for item in dob])

        #slicing out the digits to keep and str of *
        ssn = complete_data[3]
        slice_object = slice(6, 11, 1)
        ssn = ssn[slice_object]
        ssn = "***-**" + ssn

        #find the state in the dictionary imported above and change abbreviate
        state = complete_data[4]
        if state in us_state_abbrev:
            state = us_state_abbrev[state]    

        #putting it all back together
        complete_data[1] = first_name
        complete_data[2] = last_name
        complete_data[3] = dob
        complete_data[4] = ssn
        complete_data.append(state)

        print(complete_data)


#output to Analysis/employee_data.csv
csv_path = os.path.join("Analysis", "Employee_Data_Formatted.csv")
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
#will loop
    #write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    #write the second row
    csvwriter.writerow(['!214!', 'Sarah', 'Simpson', '12/04/1985', '***-**-8166', 'FL'])

#converting output to a list to be written to a text file
#file_output = dict.values(output_lines)