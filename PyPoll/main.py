#PyPoll
import csv
import os

#defining variables
candidates_vote_tally = {}
total_vote_count = 0
cand_keys = []
cand_values = []
highest_candidate_vote_count = 0
winner = ""
output_lines = {}

#reading the csv file
csv_path = os.path.join("Resources", "election_data.csv")
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

#setting up data into a dict to be output to be written to a text file
output_lines = {
                "a" : "Election Results", 
                "b" : "-------------------------",
                "c" : f"Total Votes: {total_vote_count}",
                "d" : "-------------------------",
                "e" : f"{cand_keys[0]}: {round(cand_values[0]/total_vote_count*100, 3)}% ({cand_values[0]})",
                "f" : f"{cand_keys[1]}: {round(cand_values[1]/total_vote_count*100, 3)}% ({cand_values[1]})",
                "g" : f"{cand_keys[2]}: {round(cand_values[2]/total_vote_count*100, 3)}% ({cand_values[2]})",
                "h" : f"{cand_keys[3]}: {round(cand_values[3]/total_vote_count*100, 3)}% ({cand_values[3]})",
                "i" : "-------------------------",
                "j" : f"Winner: {winner}",
                "k" : "-------------------------"
}

#printing output in terminal
for x in output_lines:
	print(output_lines[x])

#converting output to a list to be written to a text file
file_output = dict.values(output_lines)

#output to Election_Data_Analysis.txt
file_path = os.path.join("Analysis", "Election_Data_Analysis.txt")
with open(file_path, 'w') as f:
	f.write('\n'.join(file_output))


