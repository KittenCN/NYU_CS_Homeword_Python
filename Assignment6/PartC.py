import random

def add_letters(str, num):
    crlist = ''
    strAns = ''
    for i in range(26):
        crlist += chr(i + ord('A'))
    for i in range(27, 53):
        crlist += chr(i + ord('a') - 27)
    for i in range(len(str)):
        tmp = ''
        for j in range(num):
            index = random.randint(0, 51)
            tmp += crlist[index]
        strAns += str[i] + tmp
    return strAns

def remove_letters(str, num):
    strAns = ''
    for i in range(0, len(str), num + 1):
        strAns += str[i]
    return strAns

def shift_characters(str, num):
    strAns = ''
    for i in range(len(str)):
        tmp = ord(str[i]) + num
        if tmp > 127:
            tmp -= 94
        elif tmp < 32:
            tmp += 94
        strAns += chr(tmp)
    return strAns

def encode(str, num):
    return add_letters(shift_characters(str, num), num)

def decode(str, num):
    return shift_characters(remove_letters(str, num), num * -1)

if __name__ == "__main__":
    # original = "Hello!"
    # for num in range(1, 5):
    #     scrambled = add_letters(original, num)
    #     print("Adding", num, "random characters to", original, ". . .", scrambled)    
    # word1 = "HdeulHlHom!t"
    # word2 = "HTLedklFNljioMH!bi"
    # word3 = "HHHZeZrflqSflzOiosNU!jBk"
    # word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"
    # unscrambled1 = remove_letters(word1, 1)
    # print("Removing 1 characer from", word1, ". . .", unscrambled1)
    # unscrambled2 = remove_letters(word2, 2)
    # print("Removing 2 characers from", word2, ". . .", unscrambled2)
    # unscrambled3 = remove_letters(word3, 3)
    # print("Removing 3 characers from", word3, ". . .", unscrambled3)
    # unscrambled4 = remove_letters(word4, 4)
    # print("Removing 4 characers from", word4, ". . .", unscrambled4)

    # word1 = "apple"
    # newword1 = shift_characters(word1, 1)
    # print(word1, "shifted by +1 is", newword1)
    # unscrambled1 = shift_characters(newword1, -1)
    # print(newword1, "shifted by -1 is", unscrambled1)
    # word2 = "Pears are yummy!"
    # newword2 = shift_characters(word2, 2)
    # print(word2, "shifted by +2 is", newword2)
    # unscrambled2 = shift_characters(newword2, -2)
    # print(newword2, "shifted by -2 is", unscrambled2)

    n = input("(e)ncode, (d)ecode or (q)uit: ")
    if n == "e":
        num = int(input("Enter a number between 1 and 5: "))
        while num < 1 or num > 5:
            num = int(input("Enter a number between 1 and 5: "))
        str = input("Enter a phrase to encode: ")
        print("Your encoded word is: " + encode(str, num))
    elif n == "d":
        num = int(input("Enter a number between 1 and 5: "))
        str = input("Enter a phrase to decode: ")
        print("Your decoded word is: " + decode(str, num))