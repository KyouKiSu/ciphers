indexes = []
for i in range(len(string)):
    if string[i] in ' ./?!"':
        indexes.append(i)
string = self.remove_punctuation(string)
ret = ''
for (i,c) in enumerate(string):
    i = i%len(self.key)
    ret += self.i2a(self.a2i(c) - self.key[i])
for i in indexes:
    ret = ret[:i] + ' ' + ret[i:]
return ret    