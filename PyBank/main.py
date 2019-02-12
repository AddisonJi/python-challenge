import os
import csv

pybank_csv = os.path.join("..", "PyBank", "budget_data.csv")

# Open and read csv
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    # this list captures all the dollar amount and remove the first element
    newlist=[]
    # this list captures all the dollar amount and remove the last element
    secondlist=[]
    # this list stores the difference between second and the new list
    thirdlist=[]
    #total month
    totalmonth=0
    #sum of all the dollar amount
    net=0
    #sum of all the difference
    totalchange=0
    # Read through each row of data after the header
    for row in csvreader:
        totalmonth=totalmonth+1
        net=net+int(row[1])
        newlist.append(row[1])
        secondlist.append(row[1])
    #remove the first element
    newlist.pop(0)
    #remove the last element
    secondlist.pop(len(secondlist)-1)
    #difference between the two lists
    for i in range(len(newlist)):
        thirdlist.append(int(newlist[i])-int(secondlist[i]))
    #calculate the average change
    for numbers in thirdlist:
        totalchange=totalchange+numbers
    averagechange=round(totalchange/len(thirdlist),2)
    #greatest increase and decrease
    Gincrease=max(thirdlist)
    Gdecrease=min(thirdlist)

    #find the actual dollar amount by finding the index of the list that removed the first element
    GIn=str(newlist[thirdlist.index(Gincrease)])
    GDe=str(newlist[thirdlist.index(Gdecrease)])

#find the date of the greatest increase and decrease
with open(pybank_csv, newline="") as csvfile:
    readagain = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    header = next(csvfile)

    for row in readagain:
        if row[1]==GIn:
            GInDate=row[0]
        if row[1]==GDe:
            GDeDate=row[0]
    a=GInDate[:4]+ "20"+ GInDate[4:len(GInDate)] #format to Feb-2012
    b=GDeDate[:4]+ "20"+ GDeDate[4:len(GInDate)] #format to Sep-2013

#print the report in terminal
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${net}")
print(f"Average  Change: ${averagechange}")
print(f"Greatest Increase in Profits: {a} (${Gincrease})")
print(f"Greatest Decrease in Profits: {b} (${Gdecrease})")

#create the txt output
nf=open("outputPybank.txt","w")
lines=["Financial Analysis\n","--------------------------------------\n",f"Total Months: {totalmonth}\n", f"Total: ${net}\n",f"Average  Change: ${averagechange}\n",
f"Greatest Increase in Profits: {a} (${Gincrease})\n",f"Greatest Decrease in Profits: {b} (${Gdecrease})"]
nf.writelines(lines)
nf.close()

