import keyword

def checkVarname(strVarName):
    if (strVarName[0].isalpha() or strVarName[0] == '_') and strVarName.isidentifier() and not keyword.iskeyword(strVarName):
        for i in strVarName[1:]:
            if i.isalnum() or i == '_' or i.isalpha():
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    strVarName = input("Enter your Pythone variable name: ")
    if checkVarname(strVarName):
        print("This is a valid variable name")
    else:
        print("This is not a valid variable name")
