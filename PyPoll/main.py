
import os
import csv

voting_total = 0
candidates = []
candidates_votes = []
#import csv
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 
#loop through csv
    for row in csvreader:
        voting_total += 1
        if voting_total == 1:
            candidates.append(row[2])
            candidates_votes.append(1)
        else:
            try:
                icandidate = candidates.index(row[2])
                candidates_votes[icandidate] += 1
            except:
                candidates.append(row[2])
                candidates_votes.append(1)
#display voting results
results = []
results.append("Election Results\n-------------------------")
results.append(f"Total Votes: {voting_total}\n-------------------------")

candidates_winner = candidates[0]
max_voting = candidates_votes[0]
for i in range(len(candidates)):
    if candidates_votes[i] > max_voting:
        candidates_winner = candidates[i]
        max_voting = candidates_votes[i]
    percentage_of_votes = 100 * candidates_votes[i] / voting_total
    results.append(f"{candidates[i]}: {round(percentage_of_votes,3)} % ({candidates_votes[i]})")

results.append(f"-------------------------\nWinner: {candidates_winner}\n-------------------------")
#create text file to show results
filename = 'PyPollResults.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
