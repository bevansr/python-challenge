import os
import csv

election_csv = os.path.join(".", "Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first
    csv_header = next(csvfile)
    
    # Initialize tally for election variables
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    other_votes = 0
    
    # Read through each row and tally up results
    for i in election_data:
        
        # Count each vote
        total_votes += 1
        
        # Tally votes for each candidate
        if (i[2] == "Khan"):
            khan_votes += 1
        
        elif (i[2] == "Correy"):
            correy_votes += 1
        
        elif (i[2] == "Li"):
            li_votes += 1
        
        elif (i[2] == "O\'Tooley") :
            otooley_votes += 1
        # Needed in case there are formatting or spelling errors in file    
        else :
            other_votes += 1
    
    # Put candidates and their vote totals into separate lists
    candidates = ['Khan', 'Correy', 'Li', 'O\'Tooley', 'Other']
    candidate_votes = [khan_votes, correy_votes, li_votes, otooley_votes, other_votes]
    
    # Retrieve max from candidate_votes list
    most_votes = max(candidate_votes)
    
    # Get the index of max(candidate_votes) and retrieve candidate with most votes
    most_votes_index = candidate_votes.index(most_votes)
    most_votes_candidate = candidates[most_votes_index]
    
    # Use list comprehension to calculate % of vote for each candidate 
    candidate_percentage = [round(i/total_votes*100,3) for i in candidate_votes]
   
    # Check to see if there are votes for candidates other than the 4 running in the election
    if (other_votes == 0):
        
        # Remove references to other from lists
        candidates.pop(4)
        candidate_votes.pop(4)
        candidate_percentage.pop(4)
    
    else :
        # Print an alert to the terminal
        print("""Double check polling data. There shouldn't be any votes for \'other\'
--------------------------------------""")
        
    
    # Print election summary to terminal
    print("""Election Results
------------------------""")
    print(f'Total Votes: {total_votes}')
    print('------------------------')
    
    # Print the summary for each candidate
    for c, p, v in zip(candidates, candidate_percentage, candidate_votes):
        print(f'{c}: {p}% ({v})')
            
    print('------------------------')
    print(f'Winner: {most_votes_candidate}')
    print('------------------------')
        
    # Write election summary to a text file PyPoll.txt in Analysis folder
    text_summary = open("Analysis/PyPoll.txt", "w")    
    
    text_summary.write('Election Results\n')
    text_summary.write('------------------------\n')
    
     # Print the summary for each candidate
    for c, p, v in zip(candidates, candidate_percentage, candidate_votes):
        text_summary.write(f'{c}: {p}% ({v})\n')
    
    text_summary.write('------------------------\n')
    text_summary.write(f'Winner: {most_votes_candidate}\n')
    text_summary.write('------------------------\n')
    
    text_summary.close()