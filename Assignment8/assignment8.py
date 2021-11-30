import os
from decimal import Decimal
def listReadFiles(fileName):
    ans = []
    with open(fileName, 'r') as f:
        for line in f:
            if not line:
                break
            ans.append(line.strip().split(','))
    return ans

def listWriteFiles(fileName, scores):
    with open(fileName, 'w') as f:
        for s in scores:
            f.write(s[0] + ',' + str(s[1]) + '\n')

def strCheckValid(str):
    if len(str[0]) != 9 or str[0][0] != 'N':
        return "Invalid line of data: N# is invalid"
    for j in range(1, 8):
        if str[0][j].isdigit() is not True:
            return "Invalid line of data: N# is invalid"
    if len(str) != 26:
        return "Invalid line of data: does not contain exactly 26 values:"
    return "Valid"

def intCalculateScore(str):
    score = 0
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    anskey = answer_key.split(',')
    for i in range(1, len(str)):
        if str[i] == anskey[i - 1]:
            score += 4
        elif str[i] == "":
            score += 0
        else:
            score -= 1
    return score

def intCalculateMedianScore(scores):
    scores = [s[1] for s in scores]
    scores.sort()
    if len(scores) % 2 == 1:
        return scores[len(scores) // 2]
    else:
        return (scores[len(scores) // 2] + scores[len(scores) // 2 - 1]) / 2

if __name__ == '__main__':
    fileAddress = ""
    fileName = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    while os.path.exists(fileAddress + fileName + ".txt") is not True:
        print("File cannot be found.")
        fileName = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    print("Successfully opened " + fileName + ".txt")
    print("")
    content = listReadFiles(fileAddress + fileName + ".txt")
    scores = []
    invalidnum = 0
    totlascore = 0
    maxscore = 0
    minscore = 100
    print("**** ANALYZING ****")
    print("")
    for i in range(len(content)):
        strCheck = strCheckValid(content[i])
        if strCheck != "Valid":
            invalidnum += 1
            print(strCheck)
            print(content[i])
            continue
        else:
            score = intCalculateScore(content[i])
            scores.append([content[i][0], score])
            totlascore += score
            if score > maxscore:
                maxscore = score
            if score < minscore:
                minscore = score
    if invalidnum == 0:
        print("No errors found!")
    print("")
    print("**** REPORT ****")
    print("")
    print("Total valid lines of data: " + str(len(content) - invalidnum))
    print("Total invalid lines of data: " + str(invalidnum))
    print("")
    print("Mean (average) score: " + str(Decimal(totlascore / (len(content) - invalidnum)).quantize(Decimal("0.00"))))
    print("Highest score: " + str(maxscore))
    print("Lowest score: " + str(minscore))
    print("Range of scores: " + str(maxscore - minscore))
    print("Median score: " + str(Decimal(intCalculateMedianScore(scores)).quantize(Decimal("0.00"))))
    listWriteFiles(fileName + "_grades.txt", scores)