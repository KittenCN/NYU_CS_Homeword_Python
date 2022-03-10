import os
from datetime import datetime
from datetime import *

count = 3
while count:
    try:
        from tqdm import tqdm
        print("tqdm is installed")
        break
    except:
        print("tqdm is not installed")
        os.system("pip install tqdm")
        count -= 1
        if count == 0:
            print("tqdm is not installed, please install it")
            exit()
        continue
keyday = input("Enter a day(1-30): ")
keyfile1 = input("Enter the name of the 1st file: ")
keyfile2 = input("Enter the name of the 2nd file: ")
searchdate = keyfile1.split('_')[2].split('.')[0] + "-" + keyday
startdate = datetime.strptime(searchdate + " 00:00:00", "%Y-%m-%d %H:%M:%S")
enddate = datetime.strptime(searchdate + " 23:59:59", "%Y-%m-%d %H:%M:%S")
prefix = 'Taxi/'
keyfile1 = prefix + keyfile1
keyfile2 = prefix + keyfile2
keyfiles = [keyfile1, keyfile2]
result = [0] * 24
for filename in keyfiles:
    file = open(filename,'rb')
    arrFile = []
    for line in file:
        arrFile.append(line.decode('utf-8').strip().split(','))
    file.close()
    for i in tqdm(range(1, len(arrFile))):
        if datetime.strptime(arrFile[i][1], "%Y-%m-%d %H:%M:%S") >= startdate and datetime.strptime(arrFile[i][1], "%Y-%m-%d %H:%M:%S") <= enddate:
            result[datetime.strptime(arrFile[i][1], "%Y-%m-%d %H:%M:%S").hour] += 1
for i in range(24):
    print(str(i) + ":00:00 - " + str(i) + ":23:59" + ": " + str(result[i]))
with open(prefix + '[NetID]_counting_trips.txt', 'w') as f:
    f.write("For " + searchdate + "\r\n")
    for i in range(24):
        f.write(str(i) + ":00:00 - " + str(i) + ":23:59" + ": " + str(result[i]) + "\r\n")
f.close()