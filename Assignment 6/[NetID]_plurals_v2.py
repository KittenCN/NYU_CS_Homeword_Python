def make_plural(words):
    result = []
    except_str = ["roof", "belief", "chef", "chief"]
    for word in words:
        if word[-1] == 'y':
            word = word[:-1] + 'ies'
        elif word[-1] == 's':
            word = word + 'es'
        elif word[-1] == 'f' and word not in except_str:
            word = word[:-1] + 'ves'
        elif word[-2] == "fe" and word not in except_str:
            word = word[:-2] + 'ves'
        else:
            word = word + 's'
        result.append(word)
    return result

in_str = input("Enter string elements of a list separated by space: ")
list_str = in_str.split()
print(make_plural(list_str))
