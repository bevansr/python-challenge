import os
import csv

# path to csv file
bank_csv = os.path.join(".", "Resources", "budget_data.csv")

# Open and read csv
with open(bank_csv) as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first
    csv_header = next(csvfile)
    
    # Create empty lists for profit and month 
    profit_losses = []
    month = []
    
    # Initialize total_profit and months_count
    total_profit = 0
    months_count = 0
    
    # Read through each row of data after the header and add profit/loss and month values to each list
    for i in bank_data:
        profit_losses.append(int(i[1]))
        month.append(i[0])
        
        # Sum up profits as csv rows are read and list is created
        total_profit += int(i[1])
        
        # Count number of months as csv rows are read and list is created
        months_count += 1

    # Calculate avg profit
    avg_profit = round(total_profit / months_count,2)
    
    # Max and Min for profits
    max_profit = max(profit_losses)
    min_profit = min(profit_losses)
    
    # Find index of max and min profits so we can return month in summary
    max_profit_index = profit_losses.index(max_profit)
    min_profit_index = profit_losses.index(min_profit)
    
    # Message to display min/max and month each occurred in
    max_message = str(month[max_profit_index]) + ' ($' + str(max_profit) + ')'
    min_message = str(month[min_profit_index]) + ' ($' + str(min_profit) + ')'
  
    # Print summary in terminal
    print("""Financial Analysis
------------------------""")
    print(f'Total Months: {months_count} \nTotal: ${total_profit} \nAverage Change: ${avg_profit} \nGreatest increase in profits: {max_message} \nGreatest decrease in profits: {min_message}')
    
    # Write summary to a text file Pybank.txt in Analysis folder
    text_summary = open("Analysis/PyBank.txt", "w")
    
    text_summary.write('Financial Analysis\n')
    text_summary.write('------------------------\n')
    text_summary.write(f'Total Months: {months_count} \nTotal: ${total_profit} \nAverage Change: ${avg_profit} \nGreatest increase in profits: {max_message} \nGreatest decrease in profits: {min_message}')
       
    text_summary.close()
    
   