import os
import csv

totalmonths = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
previous_change = 0.0
average_change = 0

#import csv
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

#loop through csv
    for row in csvreader:
        current = float(row[1])
        if totalmonths == 0:
            greatest_increase = 0.0
            greatest_decrease = 0.0
            greatest_increase_date = row[0]
            greatest_decrease_date = row[0]
        else:
            delta = current - previous_change
            average_change += delta
            if delta > greatest_increase:
                greatest_increase = delta
                greatest_increase_date = row[0]
            elif delta < greatest_decrease:
                greatest_decrease = delta
                greatest_decrease_date = row[0]

        previous_change = current
        totalmonths += 1
        total += float(row[1])

average_change = average_change / (totalmonths-1)

#display banking results
results = []
results.append("Financial Analysis\n----------------------------")
results.append(f"Total Months: {totalmonths}")
results.append(f"Total: ${round(total)}")
results.append(f"Average Change: ${round(average_change,2)}")
results.append(f"Greatest Increase in Profits: {greatest_increase_date} (${round(greatest_increase)})")
results.append(f"Greatest Decrease in Profits: {greatest_decrease_date} (${round(greatest_decrease)})")

#create text file to show PyBank results
filename = 'PyBankResults.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')