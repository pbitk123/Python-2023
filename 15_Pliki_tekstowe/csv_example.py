import csv
import os
print(os.getcwd())

with open('data\\foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)




