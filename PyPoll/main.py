import os
import csv
import numpy as np

election_path = os.path.join('Resources', 'election_data.csv')

candidates = {}
total_votes = 0

with open(election_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

percent_votes = {}
winner = ""
max_votes = 0

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percent_votes[candidate] = percentage

    if votes > max_votes:
        max_votes = votes
        winner = candidate

winning_candidate = winner
winning_percentage = percent_votes[winner]
              
print(f"Election Results")
print("-" *25)
print(f"Total Votes: {total_votes}")
print("-" *25)
for key in percent_votes:
    print(key, ':', str(percent_votes[key]), '%', '(', candidates[key], ')')
print("-" *25)
print(f"Winner: {winner}")
print("-" *25)

with open("Election Results.txt", "w") as text:
    text.write("Election Results\n")
    text.write("-"*25 + "\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-"*25 + "\n")
    for key in percent_votes:
        text.write(f"{key}: {percent_votes[key]:.3f}% ({candidates[key]})\n")
    text.write("-"*25 + "\n")
    text.write(f"Winner: {winner}\n")
    text.write("-"*25 + "\n")





