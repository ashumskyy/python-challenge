# importing modules
import os
import csv

# declaring path to the resources
budget_path = os.path.join("Resources/budget_data.csv")

# declaring needed variables
mon_list = []
total_amnt_list = []
all_chngs_list = []

# reading the csv file from the path
with open (budget_path, 'r') as csv_budget:
    budget_reader = csv.reader(csv_budget, delimiter=",")
    
    # skip the first row (the header)
    next(budget_reader)
    
    # for loop for each row
    for row in budget_reader:
        
        # adding all the months to our list
        mon_list.append(row[0])
        
        # adding all the net total amounts to our list
        total_amnt_list.append(int(row[1]))
        
    # for loop through total amount list 
    # len - 1 so we won't get out of the range when form i+1 we subtract i
    # append all the changes to a list
    for i in range(len(total_amnt_list)-1):
        all_chngs_list.append(total_amnt_list[i + 1]-total_amnt_list[i])
   
    # find the average changes, round it to 2 decimasls
    average_chngs = round(sum(all_chngs_list)/len(all_chngs_list),2)
    
    # find the greatest increase in profit
    grt_incr = max(all_chngs_list)
    
    # find the greatest decrease in profit
    grt_decr = min(all_chngs_list)
    
    # total number of months
    ttl_months = len(mon_list)
    
    # find the net total amount of "Profit/Losses"
    net_ttl = sum(total_amnt_list)
     
    
    # looking for the index value that we need so we can find the correct month of the 
    # the greatest increase and decrease in profit
    # since our count of months is one more than the count of differences we have to +1 to the index
    incr_month_index = all_chngs_list.index(grt_incr)+1
    decr_month_index = all_chngs_list.index(grt_decr)+1
   
# print the result to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {ttl_months}")
print(f"Total: ${net_ttl}")
print(f"Average Change: ${average_chngs}")
print(f"Greatest Increase in Profits: {mon_list[incr_month_index]} (${grt_incr})")
print(f"Greatest Decrease in Profits: {mon_list[decr_month_index]} (${grt_decr})")

# path for .txt file
budget_output_path = os.path.join("analysis/budget_data.txt")

# writing a .txt file
with open(budget_output_path, 'w') as budget_output:
    budger_writer = csv.writer(budget_output)    
    
    budger_writer.writerow(["Financial Analysis"])
    budger_writer.writerow(["----------------------------"]) 
    budger_writer.writerow([f"Total Months: {ttl_months}"]) 
    budger_writer.writerow([f"Total: ${net_ttl}"]) 
    budger_writer.writerow([f"Average Change: ${average_chngs}"]) 
    budger_writer.writerow([f"Greatest Increase in Profits: {mon_list[incr_month_index]} (${grt_incr})"]) 
    budger_writer.writerow([f"Greatest Decrease in Profits: {mon_list[decr_month_index]} (${grt_decr})"]) 