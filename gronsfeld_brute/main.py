import sys
import re
sys.tracebacklimit = 0 #turn off error traceback on stop
from pycipher import Gronsfeld
from itertools import chain, product
from bisect import bisect_left

word_to_decrypt = "jemqq wpwnd"
min_key_length = 4
max_key_length = 5

min_work = 0.75

def bruteforce():
    global min_key_length
    global max_key_length
    key_set = []
    for i in range(min_key_length,max_key_length+1):
        for number in range(0,10**(i)):
            key = []
            for j in range(i):
                c = number%10
                number//=10
                key.append(c)
            key_set.append(key)
    return key_set

def search(alist, item):
    i = bisect_left(alist, item)
    if i != len(alist) and alist[i] == item:
        return i
    return -1

def hackVigenere(ciphertext):
    fo = open('C:/Users/admin/Desktop/workaround/ciphers/extras/dictionary.txt')

    ciphertext=ciphertext.lower()
    cipher_words=ciphertext.split(' ')
    word_amount=len(cipher_words)

    words = fo.readlines()
    words = list(map(str.lower,words))
    words = list(map(str.strip,words))
    fo.close()
    last = 0
    for a in bruteforce():
        GROS = Gronsfeld(a)
        if(len(a)!=last):
            print(len(a))
            last = len(a)
        i = 0
        decryptedText = GROS.decipher(ciphertext)
        for w in re.split('\.|\?| |\!',decryptedText):
            found = search(words,w.lower())
            if(found!=-1):
                i+=1
        if(i>=word_amount*min_work):
                print()
                print('Possible encryption break:')
                print('Words match:',i)
                print('Key ' ,a, ': '+decryptedText)

hackVigenere(word_to_decrypt)