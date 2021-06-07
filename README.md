# Election Analysis

## Overview of Election Audit

With the purpose of accurately measuring the votes casted during this last election, a Colorado Board of Elections tasked us in creating a program that calulates the total number of votes casted and determining a winner based on the candidate with the greatest amount of votes. We wish to look as well, an analysis of the distribution of such votes, based both on candidate as well as county. The program outputs a comprehensive summary of the distribution of votes in percentages from the total as well as their individual points. The following analysis presents a compilation of the results found when running the program given our raw ```election_results.csv``` data file.

## [Election Audit Results](analysis/election_analysis.txt)

There were a total of ***369,711*** votes casted during the election across the counties of Jefferson, Denver and Arapahoe.

### By county

The county of *Denver* had the largest turnout of voters with **306,055** votes casted in the county, accounting for **82.8%** of total votes. Second place was the county of *Jefferson* with **38,855** votes which accounted for **10.5%** of all total votes. Finally, the county of *Arapahoe* accounts for the remaining **6.7%** of total votes, tallying a total of **24,801** votes.

### By candidate

The candidate *Diana DeGette* accrued **272,892** votes, accounting for **73.8%** of all votes casted. Next is *Charles Casper Stockham* with **85,213** votes which corresponds to **23.0%** of all votes. Finally, *Raymon Anthony Doane* accrued a total of **11,606** votes, that account for 3.1% of the total votes.

The winner candidate by popular vote is **Diana DeGette** with 272,892 total votes, representing 73.8% of the total vote count.

## Election Audit Summary

The script used to analyze the results from the `election_results.csv` file managed to iterate the list of over 300,000 results in a matter of seconds and prompted a summary with the answer that we were looking for. With fast and efficient code, this script is versatile enough to analyze the results for any number of candidates in any number of counties and throw a complete analysis for all participants in all areas. Making this script an excellent tool for working with any election where the most popular candidate is the winner. However, this same script may be modified slightly to make it even more versatile to be able to work with differently formatted raw data.

1. We may modify the code to look for the specific header for the candidate/county that we look for. We can replace these two lines of code:
```
46      # Get the candidate name from each row.
47      candidate_name = row[2]
48
49      # Extract the county name from each row.
50      county_name = row[1]
```
With the following of code to extract both the county and the candidate name without having to rely on specific row numbers for that data:
```
46      # Get the candidate name from each row.
47      candidate_name = row[headers.index("Candidate")]
48
49      # Extract the county name from each row.
50      county_name = row[headers.index("County")]
```
2. Another recommendation would be an expansion of the previous point. Jumping from the fact that the method for analyzing the counties and candidate's votes are largely the same, we may place an input line at the beginning of the code so the user can specify which parameter are they looking for and the program may analyze that parameter and append any further analysis to the end of the output file with the information the are looking for (Summary of Votes, Percentage of votes, Total votes, and the parameter with the most votes). For example
```
12      parameter = input("Which parameter would you like to analyze?")
.
.
.
46      # Get the parameter name from each row. Cuts two lines of code into one
47      parameter_name = row[headers.index(parameter)]
```
These additions would make this script a very versatile tool to analyze and tally any voting information by any number of parameters.
