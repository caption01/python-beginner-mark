import os
import csv

valid_drivers = set()

with open('output/drivers.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
        passed_theory = line[2]
        if passed_theory == 'True':
            valid_drivers.add(line[0])

print(valid_drivers)        
