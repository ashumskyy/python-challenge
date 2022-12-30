# python-challenge


For this challenge, I used two slightly different approaches.

1. PyBank

For PyBank I created three lists: months list, net total amount list, and all the changes list. 
Then I appended every month to the month list and appended every net total amount to the corresponding list. 
After that, I used FOR loop in the range of length of the net total amount list and subtracted -1 from that length. In that case, when we will do the next mathematical operation we won't get out of that range. 
Then I found average changes by dividing the sum of my net total amount list by the length of the same list. 
I found a greater increase and a greater decrease in profits by using MAX and MIN functions on my newly made average changes list.
I used LEN function on my months list.
Then I found a net total amount by using SUM function on the net total amount list.
After that, I created two variables which are corresponding to the indexes I'll need to find the right month. I added +1.
Then I printed all the results to the terminal.
At last, I created a .txt file with the results.

2. PyPoll

For PyPoll I created three variables: one is a counter for total votes, the second for an empty list of our candidates, and the third one is for an empty dictionary. 
After I opened the .csv file and skipped the first header row, I used FOR loop and counted every row for the total number of votes. 
Then I created a variable for the third column in .csv file where I can grab a candidate's name.
After that, by using the IF statement, I appended the candidate's name to my candidates list. 
Also, within the same IF statement, I added the dictionary where the keys are every candidate's name and the value is 0 (number of votes). 
Because we are still in the same FOR loop, the next step was adding +1 to the values for every candidate's vote. 
Then I created an empty percentage list and used a new FOR loop to find the percentage of votes for each candidate. 
After that, I created a list of the keys from my dictionary so I can refer to the values in my results.
And finally, I found a winner by using MAX function and .get method. 
The last step was to assemble all the results together under the election results variable, print it and create a .txt file and write our results in this file.

