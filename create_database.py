# from database import *
import csv
rows = []

with open("./Data/courses.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(header)
print(rows)