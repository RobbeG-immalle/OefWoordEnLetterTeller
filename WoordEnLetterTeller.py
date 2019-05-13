from pprint import *
#import re
from string import *
def count_characters_from_file(filename):
    f = open(filename, 'r')
    d1 = dict()
    s1 = f.read()
    for c in s1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1

    pprint(d1)
def count_words_from_file(filename):
    f = open(filename, 'r')
    d2 = dict()
    s2 = f.read()
    s2 = s2.split(" ")
    # for word in s2:
    #     word = re.sub(r'[^\w\s]','',word)
    #     print(word.strip())
    for word in s2:
        word = word.strip(punctuation)
        if word in d2:
            d2[word] += 1
        else:
            d2[word] = 1
    pprint(d2)
if __name__ == '__main__':
    count_characters_from_file("Tekstfile.txt")
    count_words_from_file("Tekstfile.txt")