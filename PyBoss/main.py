#PyBoss

import csv
#so we can use the state abbreviations dict
import us_state_abbrev as us
import os

#variables
complete_data = []
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

        #converting date from YYYY-DD-MM to MM/DD/YYYY
        #origcolumn3 - will b altered
        dob = complete_data[2]
        #sperating by '-'
        dob = dob.split('-')
        year = dob[0]
        day = dob[1]
        month = dob[2]
        #putting the pieces back together in new order with a '/'
        #for x in dob:
        dob[0] = month
        dob[1] = day
        dob[2] = year       
        dob = '/'.join([str(item) for item in dob])
        #print(dob)

        #slicing out the digits to keep and appending them to str of *
        #origcolumn4 - will b altered
        ssn = complete_data[3]
        # [s for s in ssn[:-5] = '*']
        slice_object = slice(6, 11, 1)
        ssn = ssn[slice_object]
        #print(ssn)
       

        x = '***-**'.join(ssn)
        #print(x)
        #Not quite

        #origcolumn5 - State
        state = complete_data[4]
        #test = us.us_state_abbrev.keys()
        #print(test)
        
        #for i in state:
         #   if i in us.us_state_abbrev.keys():
         #       i = us.us_state_abbrev.values()
         #       print(i)
   #     for i in state:
           # if i in us.us_state_abbrev.items():
           #     i = us.us_state_abbrev.values[i]
        #for key, value in us.items():
         #   if key in state:
         #       state[value] = us.values
        #print(i)

        #can use to add new col - will just need one
        complete_data.append(state)

       

        #save back overwritting columns, samples
        for x in complete_data:
           complete_data[1] = first_name
           complete_data[2] = last_name
           complete_data[3] = dob
           complete_data[4] = ssn
           #complete_data[5] = state, being appended above
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