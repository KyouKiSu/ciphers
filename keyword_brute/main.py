import sys
import re
sys.path.insert(1, 'C:/Users/admin/Desktop/workaround/ciphers/extras')
sys.tracebacklimit = 0 #turn off error traceback on stop
import my_keyword
from itertools import chain, product
from bisect import bisect_left

word_to_decrypt = "dhdlfbjnn"
min_key_length =1
max_key_length = 7

min_work = 0.4

def bruteforce(charset):
    global min_key_length
    global max_key_length
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(min_key_length, max_key_length + 1)))

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
    for a in bruteforce('abcdefghijklmnopqrstuvwxyz'):
        if(len(a)!=last):
            print(len(a))
            last = len(a)
        i = 0
        decryptedText = my_keyword.decryptMessage(a, ciphertext)
        for w in re.split('\.|\?| |\!',decryptedText):
            found = search(words,w)
            if(found!=-1):
                i+=1
        if(i>=word_amount*min_work):
                print()
                print('Possible encryption break:')
                print('Words match:',i)
                print('Key "' + a + '": '+decryptedText)

hackVigenere(word_to_decrypt)