#PyPoll
import csv

#defining variables
candidates_vote_tally = {}
total_vote_count = 0
cand_keys = []
cand_values = []
highest_candidate_vote_count = 0
winner = ""

#reading the csv file
csv_path = ('Resources/election_data.csv')
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    #skipping header
    csv_header = next(csv_reader)

    #fill dict with candidates and votes by line
    for line in csv_reader:
        #when candidate is in dict, add one to vote count
        if line[2] in candidates_vote_tally:
                candidates_vote_tally[line[2]] += 1
        #when candidate not in dict, add to dict and assign one vote count
        else:
            candidates_vote_tally[line[2]] = 1

#use the dict to create a list of candidates and a list of votes
cand_keys = list(candidates_vote_tally.keys())
cand_values = list(candidates_vote_tally.values())
#count the total number of votes
total_vote_count = sum(candidates_vote_tally.values())
#find the candidate with the most votes
highest_candidate_vote_count = max(candidates_vote_tally.values())
#search for the key that corresponds to that number of votes
for key, value in candidates_vote_tally.items():
    if value == highest_candidate_vote_count:
        winner = key

''' 
#print analysis in terminal
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
''' 

#somesort of output problem maybe with lines vs output_lines

#add percent sign, may also multi single trunc to 3 decimals
#setting up data into a list to be output to Election_Data_Analysis.txt
a = "Election Results"
b = "-------------------------"
c = f"Total Votes: {total_vote_count}"
d = "-------------------------"
e = f"{cand_keys[0]}: {round(cand_values[0]/total_vote_count*100, 3)} ({cand_values[0]})"
f = f"{cand_keys[1]}: {round(cand_values[1]/total_vote_count*100, 3)} ({cand_values[1]})"
g = f"{cand_keys[2]}: {round(cand_values[2]/total_vote_count*100, 3)} ({cand_values[2]})"
h = f"{cand_keys[3]}: {round(cand_values[3]/total_vote_count*100, 3)} ({cand_values[3]})"
i = "-------------------------"
j = f"Winner: {winner}"
k = "-------------------------"

output_lines = [a, b, c, d, e, f, g, h, i , j, k]

#eh works diff maybe? didnt need to be ints for pybank 
#printing output to terminal
#for x in output_lines:
#	print(output_lines[x])

#output to Election_Data_Analysis.txt
file_path = ('Analysis/Election_Data_Analysis.txt')
with open(file_path, 'w') as f:
	f.write('\n'.join(output_lines))

