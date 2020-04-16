# coding: utf-8
import string

def cipher(message):
    ret = "".join([ chr(219 - ord(char)) if char in string.ascii_lowercase else char for char in message ])

    return ret

m = "The english message."
c = cipher(m)

print(c)
