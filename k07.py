# coding: utf-8

def templates(x, y, z):
    ret = "{x}時の{y}は{z}".format(x=x, y=y, z=z)
    
    return ret

s = templates(12, "気温", 22.4)

print(s)
