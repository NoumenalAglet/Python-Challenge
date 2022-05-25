#PyBoss

import csv
from datetime import datetime
#so we can use the state abbreviations dict
import us_state_abbrev as us

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
        #dunno how to use date function, all data types dont seem to work
        dob = complete_data[2]
        
        #print(type(dob))
        #for i in dob:
        #    i.strftime("%m/%d/%Y")
        #    print(i)

        #origcolumn4 - will b altered
        #dont know enough about str, would be good to overwrite range
        ssn = complete_data[3]
        # [s for s in ssn[:-5] = '*']
        
        #ast = '***-**'
        #for i in ssn:
        #    i.append(ast)

        #origcolumn5 - State
        state = complete_data[4]
        #test = us.us_state_abbrev.keys()
        #print(test)
        
        #for i in state:
         #   if i in us.us_state_abbrev.keys():
         #       i = us.us_state_abbrev.values()
         #       print(i)
        for i in state:
           # if i in us.us_state_abbrev.items():
           #     i = us.us_state_abbrev.values[i]
            for key, value in us.us_state_abbrev.items():
                if key in us.us_state_abbrev:
                    i = us.us_state_abbrev.values
        print(i)

        #can use to add new col - will just need one
        complete_data.append(state)

       

        #save back overwritting columns, samples
        for x in complete_data:
           complete_data[1] = first_name
           complete_data[2] = last_name
           complete_data[3] = dob
           complete_data[4] = ssn
           #complete_data[5] = state, being appended above
        #print(complete_data)


#x_date = datetime.now()
#print('Current Date:', x_date)
#print("mm-dd-yyyy:", x_date.strftime("%m/%d/%Y"))

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