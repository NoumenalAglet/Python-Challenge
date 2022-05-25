#PyParagraph

import csv

#defining variables

csv_path = ('Resources/election_data.csv')
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 

