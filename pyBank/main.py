import os
import csv

# create list
profit_changes = []
months = []

# set variable and initialize them
total_month = 0
total_profit = 0
current_month_profit = 0
previous_month_profit = 0
profit_change = 0

# Access the csv file 
PyBankcsv = os.path.join("Resources","pyBank_data.csv")

#Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Objective 1: The total number of months included in the dataset

    for row in csvreader:
      
      total_month = total_month + 1
      
# Objective 2: The net total amount of "Profit/Losses" over the entire period

      current_month_profit = int(row[1])
      total_profit = current_month_profit + total_profit

# Objective 3: The average of the changes in "Profit/Losses" over the entire period

      if (total_month == 1):
        
            # the value of previous month to be equal to current month
            previous_month_profit = current_month_profit
  
      else:

            # Calculate change in profit loss 
            profit_change = current_month_profit - previous_month_profit

           # Append months here. It will be used to get dates for max and min profit in entire period
            months.append(row[0])

            # Append monthly profit_loss_change to the profit_loss_changes[]
            profit_changes.append(profit_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit = current_month_profit

    #sum and average of the changes in "Profit/Losses" over the entire period
    total_profit_change = sum(profit_changes)
    average_profit = round(total_profit_change/(total_month - 1),2)


# print(average_profit)
# print(total_month)
# print(total_profit)

# Objective 4: The greatest increase in profits (date and amount) over the entire period



greatest_increase = max(profit_changes)

greatest_increase_index = profit_changes.index(greatest_increase)
greatest_increase_date = months[greatest_increase_index]

# Objective 5(a): The greatest decrease in losses (date and amount) over the entire period

greatest_decrease = min(profit_changes)
greatest_decrease_index = profit_changes.index(greatest_decrease)
greatest_decrease_date = months[greatest_decrease_index]

# print(greatest_increase)
# print(greatest_decrease)
# print(greatest_increase_date)
# print(greatest_decrease_date)


# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_month}")
print(f"Total amount of profit/losses:  ${total_profit}")
print(f"Average Change:  ${average_profit}")
print(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})")


# Export a text file with the results
results_file = os.path.join("analysis", "pyBank_data.txt")
with open(results_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_month}\n")
    outfile.write(f"Total amount of profit/losses:  ${total_profit}\n")
    outfile.write(f"Average Change:  ${average_profit}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})\n")




