def plurals(word):
    if word[-1] == 's':
        word = word + 'es'
    else:
        word = word + 's'
    return word

in_str = input("Enter string elements of a list separated by space: ")
list_str = in_str.split()
for item in list_str:
    print(plurals(item) + ' ', end='')
