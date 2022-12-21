# create var for fotes 

import os
import csv

# declaring path to the resources
election_path = os.path.join("Resources/election_data.csv")

# creatin a var for 
ttl_num_votes = 0
candidats_list = []
candidats_dict = {}

with open (election_path, 'r') as csv_election:
    election_reader = csv.reader(csv_election, delimiter=",")
    
    next(election_reader)
    
    for row in election_reader:
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

# creat election results

election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {ttl_num_votes}\n"
    f"-------------------------\n"
)

print(election_results)      
print(candidats_list)
print(candidats_dict)


election_path = os.path.join("analysis/election_data.txt")

with open (election_path, 'w') as text_file:
    # election_writer = csv.writer(election_output)
    
    text_file.write(election_results)
    