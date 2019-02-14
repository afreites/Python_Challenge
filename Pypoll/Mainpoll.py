# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import math
import operator


csvpath = os.path.join('election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
a="";
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    name=[]
    count=0
    value_counts ={}
    namecount=0
    list_name=[]
    Vote_count=0
 
    for i in csvreader:
        count=count+1
        if i[2] in value_counts:
           value_counts[name]=value_counts[name]+1
        else:
           value_counts.update([(i[2],1)])
        name=i[2]
        list_name=list(value_counts)
        Vote_count=list(value_counts.values())
        totalvotes = sum(value_counts.values())
    a+="\n................\n\nElection Results\n\n..................\n"

    a+=(f"\nTotal Votes: {count}\n..................\n")
    for list_name, Vote_count in value_counts.items():
        pct = Vote_count * 100.0 / count
        max_key = max(value_counts, key=lambda list_name: value_counts[list_name])
        summary=[(list_name, pct, Vote_count)]
        a+=(f"\n{list_name:} {pct:.2f}% ({Vote_count})\n")
    a+=(f"\n.................\n\nWinner: {max_key}\n...................\n")
  
print (a)
file = open('/Users/afreites/anaconda3/envs/pythondata/pythonchallenge/pypoll/result.txt', 'w')
file.write(a)
file.close()


    

    

