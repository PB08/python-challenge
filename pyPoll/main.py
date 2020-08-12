import os
import csv

# create list
candidates =[]
percentages = []
votes = []
# set variable and initialize them
total_vote = 0
max_index = 0

# Access the csv file 
PyPollcsv = os.path.join("Resources","pyPoll_data.csv")

#Open the CSV using the set path PyBankcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Objective 1: The total number of votes cast

    for row in csvreader:
        
          total_vote = total_vote + 1
          
          if row[2] in candidates:
              
            votes[candidates.index(row[2])] += 1

          else:

            candidates.append(row[2])
            
            votes.append(1)

max_votes = votes[0]

for count in range(len(candidates)):
      vote_percentage = votes[count]/total_vote*100
      percentages.append(vote_percentage)
      if votes[count]>max_votes:
            max_votes = votes[count]
            print(max_votes)
            max_index = count
      winner = candidates[max_index]

      percentages =[round(i,2) for i in percentages]

#print(total_vote)
#print(candidates)
#print(votes)
#print(winner)
#print(percentages)

 # Print the results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {total_vote}")
print("--------------------------")
for count in range(len(candidates)):
      print(f"{candidates[count]}: {percentages[count]}% ({votes[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")


# Export a text file with the results
results_file = os.path.join("analysis", "pyPoll_data.txt")
with open(results_file, "w") as outfile:

    outfile.write("Election Result\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes:  {total_vote}\n")
    outfile.write("----------------------------\n")
    for count in range(len(candidates)):
         outfile.write(f"{candidates[count]}: {percentages[count]}% ({votes[count]})")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner:  {winner}")
    outfile.write("----------------------------\n")
    
                 

                                           


