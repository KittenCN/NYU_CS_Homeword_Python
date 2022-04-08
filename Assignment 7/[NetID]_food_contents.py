import csv

minidict = {}
basedict = {}
file_name = "Food_contents_2019_S22.csv"
folder = "./Assignment 7/"
labels = []

def wr(fm, tup):
    result = []
    _r = []
    for item in labels:
        _r.append(item)
    result.append(_r)
    for key in tup:
        _r = []
        for _i, _item in enumerate(key[1]):
            _r.append(key[1][_item])
        result.append(_r)
    with open(folder + fm + ".csv", "w", encoding = 'latin1') as f:
        writer = csv.writer(f)
        for item in result:
            writer.writerow(item)

csv_reader = csv.reader(open(folder + file_name, encoding = 'latin1'))
for index, line in enumerate(csv_reader):
    _tup = {}
    _name = ""
    if index == 0:
        for _item in line:
            labels.append(_item.strip())
    else:
        for _index, _item in enumerate(line):
            basedict[labels[_index]] = _item.strip()
            if _index == 0:
                _name = _item.strip()
                _tup[labels[_index]] = _item.strip()
            else:
                _tup[labels[_index]] = _item.strip()
        minidict[_name] = _tup
sort1 = sorted(minidict.items(), key = lambda item:item[1]["Energy (kcal)"], reverse = True)
max_energy = sort1[0][1]["Energy (kcal)"]
wr("[NetID]_food_contents_by_energy", sort1)
for i in sort1:
    if i[1]["Energy (kcal)"] == max_energy:
        print(i[0])
sort2 = sorted(minidict.items(), key = lambda item:item[1]["Carbohydrate (g)"], reverse = False)
wr("[NetID]_food_contents_by_carbohydrate", sort2)