if __name__ == "__main__":
    n = int(input("Enter a number range: "))
    strList = ['N'] * (n + 1)
    vList = [0] * (n + 1)
    for i in range(2, n + 1):
        if vList[i] == 0:
            strList[i] = 'P'
            vList[i] = 1
            for j in range(i, n + 1, i):
                if i != j:
                    if j % i == 0:
                        strList[j] = 'N'
                        vList[j] = 1                              
    print("All prime numbers from 0 to " + str(n))
    index = 0
    for i in range(n + 1):
        if strList[i] == 'P':
            print(i, end=" ")
            index += 1
            if index % 10 == 0:
                print()