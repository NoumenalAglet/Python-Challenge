#PyBank
import csv
import os

#Variables
month_counter = 1
#for modularity, this value is set below, at line 30
old_monthly_profit = 0
new_monthly_profit = 0
net_total = 0
profit_change = 0
current_highest_change = 0
month_highest_change = ""
current_lowest_change = 0
month_lowest_change = ""
sum_profit_changes = 0
average_profit_change = 0
output_lines = {}
first_line = True

#reading the csv file
csv_path = os.path.join("Resources", "budget_data.csv")
with open(csv_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',') 
	#skipping header
	next(csv_reader)

	#finds the 1st row and saves the profit value so there is no change calc. at line 38
	for line in csv_reader:
		if first_line == True:
			old_monthly_profit = int(line[1])
			first_line = False

			for line in csv_reader:
				#count every line for number of months
				month_counter += 1
				new_monthly_profit = int(line[1])
				#finding the change of profits each month
				profit_change = new_monthly_profit - old_monthly_profit
				#recording highest or lowest change and corresponding month if record is broken
				if profit_change >= current_highest_change:
					current_highest_change = profit_change
					month_highest_change = line[0]
				elif profit_change < current_lowest_change:
					current_lowest_change = profit_change
					month_lowest_change = line[0]
				#resetting monthly profit values for next iteration
				old_monthly_profit = new_monthly_profit
				#adding up all the changes in profit
				sum_profit_changes += profit_change
				#adding up the total amounts of profit
				net_total += old_monthly_profit
			#Working out the average change of profits, using the no. of months -1, as no change occuring during first month
			average_profit_change = sum_profit_changes / (month_counter-1)

#creating output for printing and new analysis text file
output_lines = {
				"a" : "Financial Analysis",
				"b" : "----------------------------",
				"c" : f"Total Months: {month_counter}",
				"d" : f"Total: ${net_total}",
				"e" : f"Average Change: ${round(average_profit_change, 2)}",
				"f" : f"Greatest Increase in Profits: {month_highest_change} (${current_highest_change})",
				"g" : f"Greatest Decrease in Profits: {month_lowest_change} (${current_lowest_change})",
}

#printing output to terminal
for x in output_lines:
	print(output_lines[x])

#converting output to a list to be written to a text file
file_output = dict.values(output_lines)

#writting analysis text file
file_path = os.path.join("Analysis", "Budget_Data_Analysis.txt")
with open(file_path, 'w') as f:
	f.write('\n'.join(file_output))


	










