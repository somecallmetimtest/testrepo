__author__ = 'timbauer'

import csv



teams = []

# teamName = (raw_input("Select Team initials: "))
with open('LoLData.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
#    for row in reader:
#        if teamName == row['Team']:
#            print(row['Name'], row['Team'])
    for row in reader:
        if not (row['Team'] in teams):
            teams.append(row['Team'])

    print teams

print "\nhaha, I have conqured!!!"

print "\nand this would be a new branch\n"
