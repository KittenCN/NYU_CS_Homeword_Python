import csv
import os

file_name = input("Enter the name of the file: ")
prices = []
folder = "./Assignment 6/"
with open(folder + file_name) as f:
    for index, line in enumerate(f):
        _goods = []
        if index == 0:
            _goods = line.split('\t')
        else:
            _goods = line.split()
        prices.append(_goods)
price_table = prices.copy()
in_colnum = input("Enter the column number: ")
colnum = ["0", "0"]
if in_colnum is not None:
    colnum = in_colnum.split(",")
result = []
for row_index, row_item in enumerate(price_table):
    _row_result = []
    for col_index, col_item in enumerate(row_item):
        if col_index == 0 or (col_index >= int(colnum[0]) and col_index <= int(colnum[1])):
            _row_result.append(col_item)
    result.append(_row_result)
new_file_index = 1
while os.path.exists(folder + file_name[:-4] + '[' + str(new_file_index) + "].csv"):
    new_file_index += 1
with open(folder + file_name[:-4] + '[' + str(new_file_index) + "].csv", "w") as f:
    writer = csv.writer(f)
    for item in result:
        writer.writerow(item)
            