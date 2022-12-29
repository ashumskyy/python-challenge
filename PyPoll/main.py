# create var for fotes 

import os
import csv

# declaring path to the resources
election_path = os.path.join("Resources/election_data.csv")

# creatin a var for 
ttl_num_votes = 0
candidats_list = []
candidats_dict = {}

# read the csv file
with open (election_path, 'r') as csv_election:
    election_reader = csv.reader(csv_election, delimiter=",")
    
    # skip the first row (the header)
    next(election_reader)
    
    # for loop through the entire csv file to find needed values
    for row in election_reader:
        
        # counting total number of the votes
        ttl_num_votes += 1
        
        # creat a var for candidates name
        cand_name = row[2]
        
        # if the candidates not in the list
        if cand_name not in candidats_list:
            
            # add it
            candidats_list.append(cand_name)
            
            # tracking votes
            candidats_dict[cand_name] = 0
            
        # count candidates 
        candidats_dict[cand_name] = candidats_dict[cand_name] + 1


    # empty percentage list where we will append the result
    percentage_list = []

    # for loop to calculate precentage of the votes for each candidate
    for value in candidats_dict.values():
        percentage_list.append((value*100)/ttl_num_votes)

# a list of the keys from the dictionary to refer to the values
keys = list(candidats_dict)

# find the winner from our dictionary based on the max value
winner = max(candidats_dict, key=candidats_dict.get)

# creat election results
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {ttl_num_votes}\n"
    f"-------------------------\n"
    f"{candidats_list[0]}: {round(percentage_list[0], 3)}% ({candidats_dict[keys[0]]})\n"
    f"{candidats_list[1]}: {round(percentage_list[1], 3)}% ({candidats_dict[keys[1]]})\n"
    f"{candidats_list[2]}: {round(percentage_list[2], 3)}% ({candidats_dict[keys[2]]})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# print the result to the terminal
print(election_results)


# write the result to .txt file
election_path = os.path.join("analysis/election_data.txt")

with open (election_path, 'w') as text_file:
    
    text_file.write(election_results)
    