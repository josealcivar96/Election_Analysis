# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote

# import dependencies
import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join('resources', 'election_results.csv')

# assign a variable for the file to be saved to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# open the election results and read the file
with open(file_to_load) as election_data:

    # to do: read and analyse the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print header row
    headers = next(file_reader)
    print (headers)

    # print each row in the CSV file
#    for row in file_reader:
#        print(row)


# using the with statement open the file as a text file
#with open(file_to_save,'w') as txt_file:
    #write data to the file
    #txt_file.write("Counties in the Election:\n------------------------\Arapahoe\nDenver\nJefferson")
