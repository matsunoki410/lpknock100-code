# coding: utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

n = (1, 5, 6, 7, 8, 9, 15, 16, 19)

words = s.split(" ")
element_dict = dict()

for i, word in enumerate(words):
    if i + 1 in n:
        element_name = word[:1]
    else:
        element_name = word[:2]

    element_dict[element_name] = i + 1

for key in element_dict:
    print(key, element_dict[key])
