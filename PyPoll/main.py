import os
import csv
import numpy as np

election_path = os.path.join('Resources', 'election_data.csv')

candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)

    for row in csv_reader:
    
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
 
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]
              

print(f"Election Results")
print("-" *25)
print(f"Total Votes: {total_votes}")
print("-" *25)
for key in range(len(candidates)):
    print(key,':' , str(percent_votes[key]),'%','  ','(',num_votes[key],')')
print("-" *25)
print(f"Winner: {winner}")
print("-" *25)

with open("Election Results.txt", "w") as text:
    text.write(f"Election Results\n")
    text.write("-"*25 + "\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-"*25 + "\n")
for key, value in candidates.items():
    text.write(f"{key}: {str(percent_votes[key])}%   ({num_votes[key]})\n")
    text.write("-"*25 + "\n")
    text.write(f"Winner: {winner}\n")
    text.write("-"*25 + "\n")