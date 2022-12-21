#importing modules
import os
import csv

#declaring path to the resources
budget_path = os.path.join("Resources/budget_data.csv")

#declaring needed variables
mon_list = []
total_amnt_list = []
all_chngs_list = []



#reading the csv file from the path
with open (budget_path, 'r') as csv_budget:
    budget_reader = csv.reader(csv_budget, delimiter=",")
    
    
    next(budget_reader)
    
    for row in budget_reader:
        
        #adding months to our list
        
        mon_list.append(row[0])
        
        #list of net total amount
        total_amnt_list.append(int(row[1]))
        
        #lsit with all changes in Profit/Losses
    for i in range(len(total_amnt_list)-1):
        all_chngs_list.append(total_amnt_list[i + 1]-total_amnt_list[i])
   
    average_chngs = round(sum(all_chngs_list)/len(all_chngs_list),2)
    
    grt_incr = max(all_chngs_list)
    grt_decr = min(all_chngs_list)
    
    ttl_months = len(mon_list)
    net_ttl = sum(total_amnt_list)
     
    
    #searching for the index we need to find correct month of the the greatest increase and decrease
    incr_month_index = all_chngs_list.index(grt_incr)+1
    decr_month_index = all_chngs_list.index(grt_decr)+1
   
#printing the result to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {ttl_months}")
print(f"Total: ${net_ttl}")
print(f"Average Change: ${average_chngs}")
print(f"Greatest Increase in Profits: {mon_list[incr_month_index]} (${grt_incr})")
print(f"Greatest Decrease in Profits: {mon_list[decr_month_index]} (${grt_decr})")


budget_output_path = os.path.join("analysis/budget_data.txt")

with open(budget_output_path, 'w') as budget_output:
    budger_writer = csv.writer(budget_output)    
    
    budger_writer.writerow(["Financial Analysis"])
    budger_writer.writerow(["----------------------------"]) 
    budger_writer.writerow([f"Total Months: {ttl_months}"]) 
    budger_writer.writerow([f"Total: ${net_ttl}"]) 
    budger_writer.writerow([f"Average Change: ${average_chngs}"]) 
    budger_writer.writerow([f"Greatest Increase in Profits: {mon_list[incr_month_index]} (${grt_incr})"]) 
    budger_writer.writerow([f"Greatest Decrease in Profits: {mon_list[decr_month_index]} (${grt_decr})"]) 