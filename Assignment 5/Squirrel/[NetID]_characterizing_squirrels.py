import os
while True:
    filename = input("Enter the name of the file: ")
    prefix = 'Squirrel/'
    filename = prefix + filename
    if filename == "":
        print("Invalid input.")
        exit()
    file = open(filename,'rb')
    arrFile = []
    for line in file:
        arrFile.append(line.decode('utf-8').strip().split(','))
    file.close()
    colname = input("Enter the name of the column: ")
    keywords = input("Enter the keywords: ").split(',')
    colindex = -1
    sum1 = sum2 = sum3 = 0
    for i in range(len(arrFile)):
        for j in range(len(arrFile[i])):
            if arrFile[i][j] in keywords:
                sum1 += 1
                break
    dict = {}
    for key in keywords:
        dict[key] = dict.get(key, 0) + 1
    for item in dict:
        sum2 += dict[item]
    for i in range(len(arrFile[0])):
        if arrFile[0][i] == colname:
            colindex = i
            break
    for i in range(len(arrFile)):
        if arrFile[i][colindex] in keywords:
            sum3 += 1
    strResult = "For " + colname + ":" + ','.join(keywords) + "\r\n" +  "lines with the queryanywhere: " + str(sum1) + "\r\n" + "total occurrences of the query in the file: " + str(sum2) + "\r\n" + "total number of lines with the query in the requested column: " + str(sum3) + "\r\n"
    print(strResult)
    with open(prefix + '[NetID]_squirrels_chars.txt', 'w') as f:
        f.write(strResult)
    f.close()