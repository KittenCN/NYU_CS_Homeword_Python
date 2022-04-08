import operator

minidict = {}
file_name = "House_of_representatives_117 S22.csv"
prices = []
folder = "./Assignment 7/"
labels = []
info = [[] for i in range(6)]
with open(folder + file_name, encoding = 'windows-1252') as f:
    for index, line in enumerate(f):
        _goods = line.split(',')
        if index == 0:
            for _item in _goods:
                labels.append(_item.strip())
        else:
            for _index, _item in enumerate(_goods):
                info[_index].append(_item.strip())
for index, items in enumerate(info):
    minidict[labels[index]] = items
tinydict = {}
for index in range(len(minidict["District"])):
    _tup = ()
    item = {}
    for key in minidict:
        item[key] = minidict[key][index]
        if key == "District":
            _str = item[key].split(' ')
            _sum = 0
            strdis = ""
            for _s in _str:
                _f = False
                for cr in _s:
                    if cr > '0' and cr < '9':
                        _f = True
                        _sum = _sum * 10 + int(cr)
                    else:
                        break
                if _f == False:
                    strdis += _s + ' '
            _tup = (strdis.strip(), _sum)
    tinydict[_tup] = item
while True:
    state = input("Enter the state: ")
    if len(state) <= 0:
        break
    district = input("Enter the district: ") or '0'
    searchtup = (state, int(district))
    searchflag = False
    for _item in tinydict:
        if operator.eq(_item, searchtup):
            print("The representative for district {} in the state of {} is {}. The phone number is {}.".format(state, district, tinydict[_item]["Family name"] + ' ' + tinydict[_item]["Given name"], tinydict[_item]["Phone"]))
            searchflag = True
    if searchflag is False:
        print("No representative was found for district {} in the state of {}.".format(district, state))