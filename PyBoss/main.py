#PyBoss

import csv
from us_state_abbrev import us_state_abbrev
import os

#variables
line = []
id = ""
name = ""
dob = ""
ssn = ""
state = ""
complete_data = []

#open employee_data.csv from Resources folder
csv_path = os.path.join("Resources", "employee_data.csv")
with open(csv_path) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    #skipping header
    csv_header = next(csv_reader)

    #cumulatively storing each line into a column, altering as required
    for line in csv_reader:
        id = line[0]
        
        #splitting name then storing in different variables
        name = line[1]
        name = name.split()
        first_name = name[0]
        last_name = name[1]

        #converting date from YYYY-MM-DD to MM/DD/YYYY
        dob = line[2]
        #sperating by '-'
        dob = dob.split('-')
        year = dob[0]
        day = dob[1]
        month = dob[2]
        #putting the pieces back together in new order with a '/'
        dob[0] = day
        dob[1] = month
        dob[2] = year       
        dob = '/'.join(dob)

        #slicing out the digits to keep and adding to str of *
        ssn = line[3]
        slice_object = slice(6, 11, 1)
        ssn = "***-**" + ssn[slice_object]

        #finding the state in the dictionary imported above and abbreviating
        state = line[4]
        if state in us_state_abbrev:
            state = us_state_abbrev[state]    

        #putting it all back together
        line[1] = first_name
        line[2] = last_name
        line[3] = dob
        line[4] = ssn
        line.append(state)

        #appending value to complete_data, to be used when outputting file
        complete_data.append(line)

#writing to new employee_data.csv file in Formatted_Output folder
csv_path = os.path.join("Formatted_Output", "employee_data.csv")
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    for x in complete_data:
        csvwriter.writerow(x)
