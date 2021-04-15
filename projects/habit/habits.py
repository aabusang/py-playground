import sys
import csv

habits = []

with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    for row in reader:
          habits.append(row)


for habit in habits:
          print(habit)
