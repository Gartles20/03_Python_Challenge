# -*- coding: UTF-8 -*-
"""PyPoll Homework 3 """
# Import modules
import csv
import os

# Files to load and output
file_to_load = "./Resources/election_data.csv"  # Input file path
file_to_output = "election_analysis.txt" # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


# Define list and dictionary to track candidate names and vote counts
candidate_dict = {}
candidate_names = []


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Skip the header row
    header = next(reader)
    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row and grab the vote from that row
        total_votes += 1
        curr_name = row[2]

        # If the candidate is already in the candidate list, add 1 to their vote count 
        if curr_name in candidate_names:
            candidate_dict.update({curr_name:candidate_dict.get(curr_name)+1})
        # If the candidate is not in the list, add them to candidate_names and candidate_dict and set their vote count to 1
        else:
            candidate_dict.update({curr_name:1})
            candidate_names.append(curr_name)

    #move on to the next vote

#Next, figure out who won while building a percentage dictionary for each candidate.
#initialize some vars
pct_dict = {}
curr_winner = ""
curr_winner_votes = 0

for name in candidate_dict.keys():
    #Add an item to pct_dict
    pct_dict.update({name:round(candidate_dict.get(name)*100/total_votes,3)})
    # if (name) has more votes than the current winner, swap the tracking variables
    if curr_winner_votes < candidate_dict.get(name):
        curr_winner_votes = candidate_dict.get(name)
        curr_winner = name
#move on to the next name


#Building the output string piece by piece
    #First, header and total vote count
    output = f"""Election Results
    _________________________

    Total Votes = {total_votes}
    ___________________________
    """
    #Next, loop through the candidates and build the leaderboard.
    for name in candidate_dict.keys():
        output += f""" 
        {name}: {pct_dict.get(name)}% ({candidate_dict.get(name)})"""

    #Add the winning candidate stament to complete the output
    output += f"""
    __________________________

    Winning Candidate: {curr_winner} with {curr_winner_votes} votes"""


# Open a text file and save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# Print  to terminal
print(output)
