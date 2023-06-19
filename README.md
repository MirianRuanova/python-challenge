# python-challenge

# PyBank

This project involves analyzing the financial records of your company using a dataset called "budget_data.csv". The dataset consists of two columns: "Date" and "Profit/Losses". Your task is to create a Python script that performs the following financial analysis:

1. Calculate the total number of months included in the dataset.
2. Determine the net total amount of "Profit/Losses" over the entire period.
3. Calculate the changes in "Profit/Losses" over the entire period and find the average of those changes.
4. Identify the greatest increase in profits (date and amount) over the entire period.
5. Identify the greatest decrease in profits (date and amount) over the entire period.

## Getting Started

To run the code and analyze the financial records, follow these steps:

1. Ensure you have the "budget_data.csv" file available.
2. Place the "budget_data.csv" file in the "Resources" folder of the project.
3. Open the Python script in your preferred development environment.
4. Run the script.

## Code Explanation

The code starts by importing the necessary libraries and defining the path to the CSV file containing the financial data. It then reads the CSV file using the ``csv.reader`` function and extracts the header.

Next, the code initializes variables and lists to store the relevant data. It iterates over each row in the CSV file, incrementing the month count and storing the dates and profit/loss values in separate lists.

The code calculates the total number of months included in the dataset and determines the net total amount of "Profit/Losses" over the entire period by summing up the values.

It then calculates the changes in "Profit/Losses" over the entire period and stores them in a list. The average change is calculated by dividing the sum of changes by the number of changes.

The code identifies the greatest increase and decrease in profits by iterating through the list of changes, comparing the values, and storing the corresponding dates.

Finally, the code writes the financial analysis results to an output file called "output.txt" in the "analysis" folder. The output includes the total number of months, the average change, and the greatest increase and decrease in profits with their respective dates.

## Output

The financial analysis results will be saved in the "output.txt" file located in the "analysis" folder. The output will be in the following format:

```
Financial Analysis
____________________________________________
Total Months: [number of months]
Average Change: [average change]
Greatest Increase in Profits: [date] ($[amount])
Greatest Decrease in Profits: [date] ($[amount])
```

# PyPoll

This project involves analyzing a set of poll data stored in a CSV file named "election_data.csv". The dataset consists of three columns: "Voter ID", "County", and "Candidate". The goal is to create a Python script that performs the following analysis:

1. Determine the total number of votes cast.
2. Generate a complete list of candidates who received votes.
3. Calculate the percentage of votes each candidate won.
4. Calculate the total number of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Getting Started

To run the code and analyze the election data, follow these steps:

1. Ensure you have the "election_data.csv" file available.
2. Place the "election_data.csv" file in the "Resources" folder of the project.
3. Open the Python script in your preferred development environment.
4. Run the script.

## Code Explanation

The code starts by importing the necessary libraries and defining the path to the CSV file containing the election data. It then reads the CSV file using the ``csv.reader`` function and extracts the header.

Next, the code initializes variables and lists to store the relevant data. It iterates over each row in the CSV file, incrementing the vote count and storing the candidate names and ballot IDs in separate lists.

The code calculates the total number of votes cast and generates a set of unique candidate names.

It then determines the total number of votes each candidate won by counting the occurrences of each candidate in the list of votes.

To find the winner, the code iterates through the list of candidates and their total votes, comparing the values to identify the candidate with the most votes.

Finally, the code writes the analysis results to an output file called "output.txt" in the "analysis" folder. The output includes the total number of votes, the percentage of votes each candidate won, and the name of the winner.

## Output

The analysis results will be saved in the "output.txt" file located in the "analysis" folder. The output will be in the following format:

```
Election Results
____________________________________________
Total Votes: [number of votes]
____________________________________________
[Candidate 1], [percentage of votes]% ([total votes])
[Candidate 2], [percentage of votes]% ([total votes])
...
____________________________________________
Winner: [candidate name]
____________________________________________
```

