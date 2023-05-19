import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    elections = list(csvreader)
    number_votes= 0
    candidate_list=[]
    ballot_id_list=[]
    for row in elections:
        number_votes += 1
        candidate_list.append(row[2])
        ballot_id_list.append(int(row[0]))
    print("Total votes: ", number_votes)

    #Complete list of candidates who received votes.
    candidates= set(candidate_list)
    print(candidates)
    print(len(candidates))

    #Total of votes each candidate won.
    candidates_votes= list(zip(candidate_list,ballot_id_list))
    print(len(candidates_votes))

    candidates_total_votes= []
    for c in candidates:
        counter = 0
        for i in candidates_votes:
            if c==i[0]:
                counter=counter + 1
        candidates_total_votes.append([c,counter])
    print(candidates_total_votes)

    max_votes= 0
    max_candidate=""
    for max in candidates_total_votes:
        if max[1]>max_votes:
            max_votes=max[1]
            max_candidate=max[0]
    print("Winner: ", max_candidate)
    
   

output_file=os.path.join("analysis","output.txt")
with open(output_file,"w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("____________________________________________\n")
    datafile.write("Total Votes: " + str(number_votes) + "\n")
    datafile.write("____________________________________________\n")
    for i in candidates_total_votes:
        datafile.write(i[0]+ ", " + str((i[1]/number_votes)*100) + "% " + "("+ str(i[1]) + ").\n")
    datafile.write("____________________________________________\n")
    datafile.write("Winner: " + str(max_candidate) +"\n")
    datafile.write("____________________________________________\n")

    


















    # diana_total_votes_list= []
    # charles_total_votes_list=[]
    # raymon_total_votes_list=[]


    # for votes in candidates_votes:
    #     if votes[0]== "Diana DeGette":
    #         diana_total_votes_list.append(votes[1])
    #     if votes[0]== "Raymon Anthony Doane":
    #         charles_total_votes_list.append(votes[1])
    #     if votes[0]== "Charles Casper Stockham":
    #         raymon_total_votes_list.append(votes[1])

    # total_votes_for_diana =0 
    # for i in diana_total_votes_list:
    #     total_votes_for_diana = total_votes_for_diana + 1
    # print(total_votes_for_diana)


    
    




    
    

