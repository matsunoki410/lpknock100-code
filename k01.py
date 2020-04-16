# coding: utf-8

s = "パタトクカシーー"

partial_string = ''.join([c for i, c in enumerate(s) if i in (1, 3, 5, 7)])

print(partial_string)
