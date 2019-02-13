import os
import csv

pypoll_csv = os.path.join("..", "PyPoll", "election_data.csv")
output=open("outputPyPoll.txt","w")

summary={}
totalvotes=0
votes=[]
# Open and read csv
with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    for row in csvreader:
        totalvotes+=1
        if row[2] in summary.keys():
            summary[row[2]]+=1
        else:
            summary[row[2]]=1
    print("Election Results")
    output.writelines("Election Results\n")

    print("---------------------------------------------")
    output.writelines("---------------------------------------------\n")

    print(f"Total Votes: {totalvotes}")
    output.writelines(f"Total Votes: {totalvotes}\n")

    print("---------------------------------------------")
    output.writelines("---------------------------------------------\n")

    f"Total Votes: {totalvotes}"
    for key in summary:
        print (key, ":",round(((summary[key]/totalvotes)*100),3) ,"%", "(",summary[key],")")

        a=key, ": ",str(round(((summary[key]/totalvotes)*100),3)) ,"% ", "(",str(summary[key]),")\n"
        output.writelines(a)

        votes.append(summary[key])
    print("---------------------------------------------")
    output.writelines("---------------------------------------------\n")
    for key in summary:
        if summary[key]==max(votes):
            print ("Winner: ", key)
            b="Winner: ", key,"\n"
            output.writelines(b)
    print("---------------------------------------------")
    output.writelines("---------------------------------------------\n")


output.close()

