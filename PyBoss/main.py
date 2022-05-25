#PyBoss

import csv
from hashlib import new
#from operator import index #?

#variables
temp_row = []
new_row_list = []
old_row_list = []
test_append = []
#open Resources/employee_data.csv
csv_path = ('Resources/employee_data.csv')
with open(csv_path) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    #skipping header
    csv_header = next(csv_reader)

  
    for line in csv_reader:
        #save into columns
        #name
        column1 = line[0]
        column2 = line[1]
        column3 = line[2]
        column4 = line[3]
        column5 = line[4]
        #print(column5)

        #alter stuff

        #save back overwritting columns
        for x in line:
           line[0] = column1
           line[4] = column2
        print(line)



        #made list
        #old_row_list = list(line)
        #print(old_row_list)
        #saved all of index[0] into variable
        #new_row_list = old_row_list.append(line)
        #print(new_row_list)
        #test var to append
        #test_append = old_row_list[1]
        #print(test_append)

        #for i in old_row_list:
        #    old_row_list.append(test_append[i])
        #    print(old_row_list)



        #print(old_row_list[0])
        #print(new_row_list)

        #zipped = zip(new_row_list, test_append)
        #print(list(zipped))



        #new_row_list = list(i)
        #new_row_list = i[4][0]

        #new_row_list = list(i)
        #new_row_list = i[0]
        #temp_var = i[1] + "hat" #split name
        #new_row_list.append(temp_var) #hmm
        #print(new_row_list)
        #print(temp_var)
    



        #append as we go?
        #new_row_list.append(old_row_list[0])

        #print(old_row_list)


        #print(temp_row[1])
        # = temp_row["overwrite"]

        #save rows as lists, maybe not nec








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