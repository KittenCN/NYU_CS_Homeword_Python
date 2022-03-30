file_add = "Assignment 4/alphabet.txt"
def encrypt(key, plaintext):
    file = open(file_add,'rb')
    key = int(key)
    arrfile = []
    for line in file:
        arrfile.append(line.decode('utf-8').strip().split(','))
    file.close()
    result = ""
    for i in range(len(arrfile[0])):
        t = ""
        for j in range(len(arrfile[0][i])):
            if arrfile[0][i][j] != '"'  and arrfile[0][i][j] != ' ':
                t += arrfile[0][i][j]
        t.replace(" ","")
        arrfile[0][i] = t
    for i in range(len(plaintext)):
        index = arrfile[0].index(plaintext[i]) + key
        if index > len(arrfile[0]) - 1:
            index = index - len(arrfile[0])
        result += arrfile[0][index]
        result.replace(" ","")
    return result

def decrypt(key, ciphertext):
    file = open(file_add,'rb')
    key = int(key)
    arrfile = []
    for line in file:
        arrfile.append(line.decode('utf-8').strip().split(','))
    file.close()
    result = ""
    for i in range(len(arrfile[0])):
        t = ""
        for j in range(len(arrfile[0][i])):
            if arrfile[0][i][j] != '"' and arrfile[0][i][j] != ' ':
                t += arrfile[0][i][j]
        t.replace(" ","")
        arrfile[0][i] = t
    for i in range(len(ciphertext)):
        st = ciphertext[i].replace(" ","")
        index = arrfile[0].index(st) - key
        if index < 0:
            index = index + len(arrfile[0])
        result += arrfile[0][index]
        result.replace(" ","")
    return result