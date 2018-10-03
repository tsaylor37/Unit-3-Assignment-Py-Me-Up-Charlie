'''Ojective: To modernize vote-counting process. Displaying total number of votes cast, complete list of candidates which received votes,
    percentage of voted each candidate won, total number of votes each candidate won, and winner of election.'''


#I will be using the "Voter ID", "County"and "Candidate" info from the election_data.csv dataset.

import os
import csv


#Path to collect data from dataset file
electionCSV = os.path.join("..","PyPoll", "election_data.csv")

# Track various voting parameters
total_votes = 0

#Read in CSV file
with open(electionCSV) as f:
    reader = csv.DictReader(f)

    for row in reader:
    
        # Track the total
        total_votes = total_votes + 1
          
#Displaying output to terminal    
print(f"Elections Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"----------------------------")
print(f"Winner: ")
print(f"----------------------------")




output = os.path.join("..", "PyPoll", "election_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w', newline='') as csvfile:

   # Initialize csv.writer
   csvwriter = csv.writer(csvfile, delimiter=',')

   # Write the first row (column headers)
   csvwriter.writerow(['Elections Results'])

   # Write the second row
   csvwriter.writerow(['----------------------------'])

   # Write the third row
   csvwriter.writerow(['Total Votes: {total_votes}'])  

 # Write the fourth row (column headers)
   csvwriter.writerow(['----------------------------'])

   # Write the fifth row
   csvwriter.writerow(['----------------------------'])

   # Write the sixth row
   csvwriter.writerow(['Winner: '])  

     # Write the seventh row
   csvwriter.writerow(['----------------------------'])