import csv

minidict = {}
file_name = "car_equipment.csv"
folder = "./Assignment 7/"

def wr(new_file_index, tup):
    result = []
    _r = []
    _i = "id"
    _y = "year"
    _r.append(_i)
    _r.append(_y)
    result.append(_r)
    for key in tup:
        _r = []
        _r.append(key)
        _r.append(tup[key])
        result.append(_r)
    with open(folder + file_name + '[' + str(new_file_index) + "].csv", "w") as f:
        writer = csv.writer(f)
        for item in result:
            writer.writerow(item)

with open(folder + file_name, encoding = 'windows-1252') as f:
    for index, line in enumerate(f):
        _goods = line.split(',')
        if index != 0:
            if _goods[3] != "NULL":
                minidict[int(_goods[0].replace('\'', ''))] = int(_goods[3].replace('\'', ''))
            else:
                minidict[int(_goods[0].replace('\'', ''))] = 0
minidict_sort1 = {}
minidict_sort2 = {}
for i in sorted(minidict):
    if minidict[i] != 0:
        minidict_sort1[i] = minidict[i]
    else:
        minidict_sort1[i] = "NULL"
wr(1, minidict_sort1)
_sort2 = sorted(minidict.items(), key = lambda item:item[1], reverse = True)
for i in _sort2:
    if i[1] == 0:
        minidict_sort2[i[0]] = "NULL"
    else:
        minidict_sort2[i[0]] = i[1]
wr(2, minidict_sort2)
