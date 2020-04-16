# coding: utf-8

def n_gram(source, n=2):
    ret = [''.join(source[r:r+n]) for r in range(0, len(source), n)]

    return ret

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print("和集合: %s" % (X|Y,))
print("積集合: %s" % (X&Y,))
print("差集合: %s" % (X-Y,))

if 'se' in X:
    print("X は 'se' を含む")
else:
    print("X は 'se' を含まない")

if 'se' in Y:
    print("Y は 'se' を含む")
else:
    print("Y は 'se' を含まない")
