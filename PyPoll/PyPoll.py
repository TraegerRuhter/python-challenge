import csv
import os

# path for election data file.
election_CSV = os.path.join("election_data.csv")

#initial Vars
total_votes = 0
candidate_votes = {}
winner_count = 0

# read in the CSV file
with open(election_CSV) as voter_roll:
    reader = csv.reader(voter_roll)
    
    # Read and store header
    header = next(reader)

    # tally total votes and votes per candidate
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        # process new candidates
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Build the first part of the summary
election_summary = (
    f"\n\nElection Results!\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

# Process how each candidate did and add them to the summary
for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes
    vote_percentage = (votes / total_votes) * 100

    # Calculate the winner by comparing the votes to the current winner
    if votes > winner_count:
        winner_count = votes
        elected_candidate = candidate
        
    # Add the candidate to the summary
    election_summary += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

# Finish the summary with the winner
election_summary += (
    f"-------------------------\n"
    f"The winner is!!!: {elected_candidate}\n"
    f"-------------------------\n")


# Print the summary to the terminal
print(election_summary)

# Save the summary to a text file
with open(os.path.join("election_results.txt"), "w") as txt_file:
    txt_file.write(election_summary)
