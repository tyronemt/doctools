import csv

lst = []
with open("static\san_bernardino.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(row)
print(lst)