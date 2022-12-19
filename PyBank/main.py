#importing modules
import os
import csv

#declaring path to the resources
budget_path = os.path.join("Resources/budget_data.csv")

#declaring needed variables
ttl_num_mon = 0
net_ttl_amnt = 0
avrg_chge = []
grts_prof_incr = 0
grts_prof_decr = 0


#reading the csv file from the path
with open (budget_path, 'r') as csv_budget:
    budget_reader = csv.reader(csv_budget, delimiter=",")
    
    #skipping the first row (header)
    next(budget_reader)
    
    #for loop for each row
    for row in budget_reader:
        
        #total number of months
        ttl_num_mon = ttl_num_mon + 1    
        
        #net total amount of "Profit/Losses" over the entire period
        net_ttl_amnt += int(row[1])
        
        
        
        #greatest increase in profits (date and amount)
        if int(row[1]) > grts_prof_incr:
            grts_prof_incr = int(row[1])
            grts_prof_incr_result = (f"Greatest Increase in Profits: {row[0]} (${grts_prof_incr})")
        
        #greatest decrease in profits (date and amount)
        if int(row[1]) < grts_prof_decr:
            grts_prof_decr = int(row[1])
            grts_prof_decr_result = (f"Greatest Decrease in Profits: {row[0]} (${grts_prof_decr})") 
    
    
    #printing the result to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {ttl_num_mon}")
    print(f"Total: ${net_ttl_amnt}")
    print(grts_prof_incr_result)
    print(grts_prof_decr_result)
        

#declarint path to the output file
output_budget_path = os.path.join("analysis/budget_data_output.txt")

#create and open a new .txt file so we can write in it
with open (output_budget_path, 'w') as output:
    budget_writer = csv.writer(output)
    
    #writing into .txt file
    budget_writer.writerow(["Financial Analysis"])
    budget_writer.writerow(["----------------------------"])
    budget_writer.writerow([f"Total Months: {ttl_num_mon}"])
    budget_writer.writerow([f"Total: ${net_ttl_amnt}"])
    budget_writer.writerow([grts_prof_incr_result])
    budget_writer.writerow([grts_prof_decr_result])

   
   
   