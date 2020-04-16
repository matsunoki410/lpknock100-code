# coding: utf-8

def n_gram(source, n=2):
    ret = [''.join(source[r:r+n]) for r in range(0, len(source), n)]

    return ret

s = "I am an NLPer"

char_bigram = n_gram(s, 2)
word_bigram = n_gram(s.split(" "), 2)

print(char_bigram)
print(word_bigram)
