'''Ojective: To analyze the finnacial rexords to find the Total Number of Months,
Total Net Amount/Average Change of the profit/losses, with the 
greatest increase in profits and greatest decrease in losses.'''


#I will be using the "date" and "revenue" info from the budget_data dataset.

import os
import csv


#Path to collect data from dataset file
budgetCSV = os.path.join("..","PyBank", "budget_data.csv")

# Track various revenue parameters
total_months = 0
total_revenue = 0
previous_rev = 0
rev_change_list =[]
month_change = []
# Initialize a variable for greatest increase/decrease that has two items in a list. 
greatest_incr = ["", 0]
greatest_decr = ["", 0]

#Read in CSV file
with open(budgetCSV) as f:
    reader = csv.DictReader(f)

    for row in reader:
    
        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        #Comparing rows to increase/descrese.
        rev_change =  int(row["Revenue"]) - previous_rev
        #rev_change_list = rev_change_list + [rev_change]
        rev_change_list.append(rev_change)
        previous_rev = int(row["Revenue"])

        # Add to list the date which corresoponds to the revenue change.
        month_change = month_change + [row["Date"]]

        # Calculate the greatest increase if true.
        if (rev_change > greatest_incr[1]):
            # Get date of greatest rev change
            greatest_incr[0] = row["Date"]
            # Add greatest_incr and list newest rev_change. 
            greatest_incr[1] = rev_change

        # Calculate greatest decrese if statement is true.
        if (rev_change < greatest_decr[1]):
            # Get the date of greatest rev change
            greatest_decr[0] = row["Date"]
            # Add to the greatest_incr and list newest rev_change. 
            greatest_decr[1] = rev_change
#Calculating the average change.
avg_rev_change = int(round(sum(rev_change_list)) / len(rev_change_list))
#Displaying output to terminal    
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${(avg_rev_change)}")
print(f"Greatest Increase in Revenue: {greatest_incr[0]} (${greatest_incr[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decr[0]} (${greatest_decr[1]})")   

#Displaying output to terminal and export to text file

output = os.path.join("..", "PyBank", "budget_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w', newline='') as csvfile:

   # Initialize csv.writer
   csvwriter = csv.writer(csvfile, delimiter=',')

   # Write the first row (column headers)
   csvwriter.writerow(['Financial Analysis'])

   # Write the second row
   csvwriter.writerow(['----------------------------'])

   # Write the third row
   csvwriter.writerow(['Total Months: {total_months}'])  

   # Write the fourth row
   csvwriter.writerow(['Total: ${total_revenue}'])  

   # Write the fifth row
   csvwriter.writerow(['Average Change: ${(avg_rev_change)}'])  

   # Write the sixth row
   csvwriter.writerow(['Greatest Increase in Revenue: {greatest_incr[0]} (${greatest_incr[1]})'])

   # Write the seventh row
   csvwriter.writerow(['Greatest Decrease in Revenue: {greatest_decr[0]} (${greatest_decr[1]})'])


        