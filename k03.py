# coding: utf-8
import string

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = s.split(" ")

alphabet_count_list = [len(list(filter(lambda char: char in string.ascii_letters, word))) for word in words]

print(alphabet_count_list)