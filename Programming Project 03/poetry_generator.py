# IAE 101
# Project 04 - Poetry Generator
# Name
# Student ID
# netid
# Date
# poetry_generator.py (v.4)

import nltk
import pronouncing
import random

# This uses the King James Bible as the corpus
# Use: nltk.corpus.gutenberg.fileids()
# to see which other gutenberg works are available.
#my_corpus = nltk.corpus.gutenberg.words('bible-kjv.txt')

# This uses all the words in the entire gutenberg corpus
#my_corpus = nltk.corpus.gutenberg.words()

# This loop constructs a corpus from all the shakespeare plays included in the
# shakespeare corpus included in NLTK
# Use: nltk.corpus.shakespeare.fileids()
# to see which shakespeare works are included.
my_corpus = []
for fid in nltk.corpus.shakespeare.fileids():
    my_corpus += nltk.corpus.shakespeare.words(fid)
bigrams = nltk.bigrams(my_corpus)
cfd = nltk.ConditionalFreqDist(bigrams)

# This function takes two inputs:
# source - a word represented as a string (defaults to None, in which case a
#          random word will be selected from the corpus)
# num - an integer (how many words do you want)
# The function will generate num random related words using
# the CFD based on the bigrams in our corpus, starting from
# source. So, the first word will be generated from the CFD
# using source as the key, the second word will be generated
# using the first word as the key, and so on.
# If the CFD list of a word is empty, then a random word is
# chosen from the entire corpus.
# The source word is always included as the first word in the result and is
# included in the count.
# The function returns a num-length list of words.
def random_word_generator(source=None, num=1):
    result = []
    while source is None or not source[0].isalpha():
        source = random.choice(my_corpus)
    word = source
    result.append(word)
    while len(result) < num:
        if word in cfd:
            init_list = list(cfd[word].keys())
            choice_list = [x for x in init_list if x[0].isalpha()]
            if len(choice_list) > 0:
                newword = random.choice(choice_list)
                result.append(newword)
                word = newword
            else:
                word = None
                newword = None
        else:
            newword = None
            while newword is None or not newword[0].isalpha():
                newword = random.choice(my_corpus)
            result.append(newword)
            word = newword
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns the number of syllables in word as an
# integer.
# If the return value is 0, then word is not available in the CMU
# dictionary.
def count_syllables(word):
    phones = pronouncing.phones_for_word(word)
    count_list = [pronouncing.syllable_count(x) for x in phones]
    if len(count_list) > 0:
        result = max(count_list)
    else:
        result = 0
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns a list of words that rhyme with
# the input word.
def get_rhymes(word):
    result = pronouncing.rhymes(word)
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns a list of strings. Each string in the list
# is a sequence of numbers. Each number corresponds to a syllable
# in the word and describes the stress placed on that syllable
# when the word is pronounced.
# A '1' indicates primary stress on the syllable
# A '2' indicates secondary stress on the syllable
# A '0' indicates the syllable is unstressed.
# Each element of the list indicates a different way to pronounce
# the input word.
def get_stresses(word):
    result = pronouncing.stresses_for_word(word)
    return result

# A test function that demonstrates how each of the helper functions included
# in this file work.  You supply a word and it will run each of the above
# functions on that word.
def test():
    keep_going = True
    while keep_going:
        word = input("Please enter a word (Enter '0' to quit): ")
        if word == '0':
            keep_going = False
        elif word == "":
            pass
        else:
            print(cfd[word].keys(), cfd[word].values())
            print()
            print("Random 5 words following", word)
            print(random_word_generator(word, 5))
            print()
            print("Pronunciations of", word)
            print(pronouncing.phones_for_word(word))
            print()
            print("Syllables in", word)
            print(count_syllables(word))
            print()
            print("Rhymes for", word)
            print(get_rhymes(word))
            print()
            print("Stresses for", word)
            print(get_stresses(word))
            print()

# Runs all the functions many times with random-ish inputs to increase
# confidence that they perform as expected.
def stress_test():
    for i in range(10000):
        wl = random_word_generator(None, 10)
        print(wl)

    wl = random_word_generator(None, 10000)
    for w in wl:
        sc = count_syllables(w)
        print(w, sc)

    wl = random_word_generator(None, 10000)
    for w in wl:
        rs = get_rhymes(w)
        print(w, len(rs))
        print(rs)

    wl = random_word_generator(None, 10000)
    for w in wl:
        stl = get_stresses(w)
        print(w, len(stl))
        print(stl)

############################################################
#                                                         #
#  STUDENT SECTION                                        #
#                                                         #
############################################################

# generate_rhyming_line()
# Complete this function so that it returns a list. The list
# must contain two strings of 5 words each. Each string
# corresponds to a line. The two lines you return must rhyme.
def generate_rhyming_lines():
    oriStrList = random_word_generator(None, 2)
    while len(oriStrList) != 2:
        oriStrList = random_word_generator(None, 2)
    ansList = [""] * 2
    intLine = 0
    for i in range(len(oriStrList)):
        intIndex = 0
        rhymeList = get_rhymes(oriStrList[i])
        for i in range(len(rhymeList)):
            if intIndex < 5:
                # print(str(intLine), str(intIndex), rhymeList[i])
                ansList[intLine] += rhymeList[i] + " "
                intIndex += 1
            else:
                intLine += 1
                break
    return ansList

# generate_10_syllable_lines()
# Complete this function so that it returns a list. The list
# must contain two strings of 10 syllables each. Each string
# corresponds to a line and each line must be composed of words
# whose number of syllables add up to 10 syllables total.
def generate_10_syllable_lines():
    ansList = [""] * 2
    intLine = 0
    for i in range(2):
        sumsyllables = 0
        while sumsyllables < 10:
            oriStrList = random_word_generator(None, 5)
            while len(oriStrList) != 5:
                oriStrList = random_word_generator(None, 5)
            for j in range(len(oriStrList)):
                sumsyllables += count_syllables(oriStrList[j])
            if sumsyllables >= 10:
                for j in range(len(oriStrList)):
                    ansList[intLine] += oriStrList[j] + " "
                intLine += 1
    return ansList


# generate_metered_line()
# Complete this function so that it returns a string. This string
# will be composed of randonly selected words, will contain 10
# syllables, and the rhythm of the line must match the following
# pattern of stresses: 0101010101
def generate_metered_line():
    num = 0
    ansList = ""
    while num < 10:
        oriStr = random_word_generator(None, 1)
        stressesList = get_stresses(oriStr[0])
        if len(stressesList) > 0:
            if stressesList[0] == "01":
                ansList += oriStr[0] + " "
                num += 1
    return ansList

# generate_line()
# Use this function to generate each line of your poem.
# This is where you will implement the rules that govern
# the construction of each line.
# For example:
#     -number of words or syllables in line
#     -stress pattern for line (meter)
#     -last word choice constrained by rhyming pattern
# Add any parameters to this function you need to bring in
# information about how a particular line should be constructed.
def generate_line(rhyme=None, intLength=1, stdstress=None):
    ansList = ""
    index = 1
    while intLength > 0:
        stressesList = []
        oriStrList = []
        while len(stressesList) <= 0:
            if intLength == 1 and rhyme is not None:
                oriStrList = rhyme
                if index >= len(oriStrList):
                    tmp = random.randint(0, len(rhyme) - 1)
                    ansList += rhyme[tmp] + " "
                    intLength -= 1
                    break
                oriStr = [oriStrList[index]]
                index += 1
            else:
                oriStr = random_word_generator(None, 1)
                if intLength == 1:
                    while len(get_rhymes(oriStr[0])) == 0:
                        oriStr = random_word_generator(None, 1)
            stressesList = get_stresses(oriStr[0])
        for i in range(len(stressesList)):
            if stressesList[i] in stdstress or stdstress is None:
                ansList += oriStr[0] + " "
                intLength -= 1
                break
    return ansList

# generate_poem()
# Use this function to construct your poem, line by line.
# This is where you will implement the rules that govern
# the structure of your poem.
# For example:
#     -The total number of lines
#     -How the lines relate to each other (rhyming, syllable counts, etc)
def generate_poem():
    intNum = 4
    intLengthList = [8, 6]
    stdstress = [["0", "00"], ["1", "01", "11"]]
    ans = ""
    strRhyme = ""
    flag = False
    for i in range(intNum):
        for j in range(2):
            if i == 0 and flag is False:
                ans += generate_line(None, intLengthList[j], stdstress[j])
                strRhyme = get_rhymes(ans.split()[-1])
                flag = True
            else:
                ans += generate_line(strRhyme, intLengthList[j], stdstress[j])
            ans += '\r\n'
    return ans


if __name__ == "__main__":
    # test()
    # stress_test()
    # print()

    # result1 = generate_rhyming_lines()
    # print(result1)
    # print()

    # result2 = generate_10_syllable_lines()
    # print(result2)
    # print()

    # result3 = generate_metered_line()
    # print(result3)
    # print()    
    my_poem = generate_poem()
    print(my_poem)