import os
import csv
import numpy as np 

budget_path = os.path.join('Resources', 'budget_data.csv')

with open(budget_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    data_list = list(csv_reader)

    data_list.remove(data_list[0])

    total_months = len(data_list)
    total = 0
    total_change = 0
    greatest_increase = 0
    date_greatest_inc = ""
    greatest_decrease = 0
    date_greatest_dec = ""

for i in range(total_months):

    total += int(data_list[i][1])

    if(i != (total_months - 1)):
        month_change = int(data_list[i + 1][1]) - int(data_list[i][1])
        total_change += month_change

    if (month_change > greatest_increase):
        greatest_increase = month_change
        date_greatest_inc = data_list[i + 1][0]
            
    if (month_change < greatest_decrease):
        greatest_decrease = month_change
        date_greatest_dec = data_list[i + 1][0]

    
print(f"Financial Analysis")
print("-" *20)
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${total_change}")
print(f"Greatest Increase in Profits: {date_greatest_inc}(${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_dec}(${greatest_decrease})")

output_file = os.path.join('analysis', 'bank_analysis.txt')

with open(output_file, "w") as text:
    text.write(f"Financial Analysis\n")
    print("-" *20 + "\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${total_change}\n")
    text.write(f"Greatest Increase in Profits: {date_greatest_inc}(${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {date_greatest_dec}(${greatest_decrease})")

