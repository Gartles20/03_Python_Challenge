# -*- coding: UTF-8 -*-
"""PyBank Homework 3"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_in = "./Resources/budget_data.csv"  # Input file path
file_to_output = "./budget_analysis.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

current_month = 0
previous_month = 0
change = 0
total_change = 0

greatest_dec = 0
greatest_dec_date = ""
greatest_inc = 0
greatest_inc_date = ""

# Open and read the csv
with open(file_in) as fin_data:
    reader = csv.reader(fin_data, delimiter = ',')

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        #increment the month count and add new row P/L to the total
        total_months +=1
        total_net += int(row[1])

        #Process the first month to set up calculating change in P/L between months
        if total_months == 1:
            previous_month = int(row[1])
        #Calculate the change in P/L and add to the total change tracker
        else:
            current_month = int(row[1])
            change = current_month - previous_month
            total_change += change
            previous_month = current_month


        #check if change is greater than greatest increase. If it is, update the increase tracking vars
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_date = row[0]

        #check if change is less than greatest decrease. If it is, update the decrease tracking vars
        elif change < greatest_dec:
            greatest_dec = change
            greatest_dec_date = row[0]

#move on to the next month


# Calculate the average net change across the months
avg_change = total_change/(total_months-1)

# Generate the output summary
output = f"""
Analysis
______________
Final Total: ${total_net}
Total Months: {total_months}
Average Change: ${avg_change}
______________
Greatest Increase: ${greatest_inc} on {greatest_inc_date}
Greatest Decrease: ${greatest_dec} on {greatest_dec_date}
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
