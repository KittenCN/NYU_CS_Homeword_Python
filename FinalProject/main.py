import csv
import datetime
import numpy as np

try:
    from tqdm import tqdm
except :
    import os
    os.system('pip3 install tqdm')
    from tqdm import tqdm

def read_csv(file_name):
    csv_reader = csv.reader(open(file_name))
    minidict = []
    split_char = ','
    labels = []
    for index, line in enumerate(csv_reader):
        _tup = []
        if index == 0:
            for _item in line:
                labels.append(_item.strip(split_char))
        else:
            for _index, _item in enumerate(line):
                _tup.append(_item.strip(split_char))
            minidict.append(_tup)
    return minidict

def never_go_above(cc, trans, mon=-1):
    result_cc = []
    sum_cc = np.zeros([len(cc), 13])
    pbar = tqdm(total=len(trans))
    for i in trans:
        pbar.update(1)
        _index = -1
        for j in cc:
            _index += 1
            if j[0] == i[0]:
                break
        sum_cc[_index, int(i[1][5:7])] += float(i[2])
    pbar.close()
    if mon == -1:
        pbar = tqdm(total=len(cc))
        for index, i in enumerate(cc):
            pbar.update(1)
            if float(i[4]) >= sum_cc[index].max():
                result_cc.append(i)
        pbar.close()
        return result_cc
    elif mon > 0 and mon < 13:
        pbar = tqdm(total=len(cc))
        for index, i in enumerate(cc):
            pbar.update(1)
            if float(i[4]) < sum_cc[index, mon]:
                result_cc.append(i)
        pbar.close()
        return result_cc

if __name__ == "__main__":
    file_name = "FinalProject/cc_info.csv"
    cc_info = read_csv(file_name)
    file_name = "FinalProject/transactions.csv"
    transactions = read_csv(file_name)
    res = never_go_above(cc_info, transactions)
    print("The list of users who hace never go above the monthly credit card limit:")
    if len(res) == 0:
        print("No one")
    else:
        for item in res:
            print(item)
    print()
    mon = datetime.datetime.today().month
    res = never_go_above(cc_info, transactions, mon)
    print("The list of users who went above their credit card monthly limit on that day")
    if len(res) == 0:
            print("No one")
    else:
        for item in res:
            print(item)
    
