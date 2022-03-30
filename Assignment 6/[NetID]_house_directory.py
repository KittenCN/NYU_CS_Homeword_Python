import re
folder = "./Assignment 6/"
file_name = "House_of_representatives_117 S22.csv"
ori_list = []
with open(folder + file_name, encoding = 'windows-1252') as f:
    for index, line in enumerate(f):
        _goods = []
        if index == 0:
            _goods = line.split(',')
        else:
            _goods = line.split(',')
        ori_list.append(_goods)
new_list = ori_list.copy()
for item in new_list:
    for index, _item in enumerate(item):
        item[index] = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])","", _item).lower()
while True:
    ask = input("Enter the state of interest : ")
    row = []
    for index, item in enumerate(new_list):
        for _item in item:
            if ask == _item:
                row.append(index)
                flag = True
                break
    if len(row) <= 0:
        print("Not found")
        break
    else:
        for index, item in enumerate(ori_list):
            if index in row:
                print(item)

        