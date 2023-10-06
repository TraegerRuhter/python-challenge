import csv
import os

#import and csv file
input_file = os.path.join("budget_data.csv")

#vars
MonthCounter = 0
Net_Total = 0
Name_of_Month = []
pl_change_tracker = []

#contabulators for highest and lowest changes and their months
Increase_Max = ["", 0]
Decrease_Max = ["", float("inf")]
        

with open(input_file) as input_data:
    Read_CSV = csv.reader(input_data)
    
    #read and store the header
    header = next(Read_CSV)

    # Read in the first row of data after the header
    First_Line = next(Read_CSV)
    MonthCounter += 1
    Net_Total += int(First_Line[1])
    Line_Before = int(First_Line[1])

    # For loop to iterate through the rows
    for Row in Read_CSV:

        # Count the number of months and sum the total
        MonthCounter += 1
        Net_Total += int(Row[1])

        # Calculate the change in profit/losses and add to the list
        PL_Change = int(Row[1]) - Line_Before
        Line_Before = int(Row[1])
        pl_change_tracker.append(PL_Change)
        Name_of_Month.append(Row[0])

        # Compare and record Greatest increase and decrease
        if PL_Change > Increase_Max[1]:
            Increase_Max = [Row[0], PL_Change]
        elif PL_Change < Decrease_Max[1]:
            Decrease_Max = [Row[0], PL_Change]

#Calculate the average change
pl_changeAvg = sum(pl_change_tracker) / len(pl_change_tracker)

###################end of contabulation

# Generate Output Summary
Output_Summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {MonthCounter}\n"
    f"Total: ${Net_Total}\n"
    f"Average Change: ${pl_changeAvg:.2f}\n"
    f"Greatest Increase in Profits: {Increase_Max[0]} (${Increase_Max[1]})\n"
    f"Greatest Decrease in Profits: {Decrease_Max[0]} (${Decrease_Max[1]})\n"
    )
print(Output_Summary)


# Export the results as a file
with open("Profit&Loss_Report.txt", "w") as txt_file:
    txt_file.write(Output_Summary)