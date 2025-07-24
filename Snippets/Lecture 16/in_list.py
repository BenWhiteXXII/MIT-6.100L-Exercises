def in_list(L, e):
    if len(L) == 0:
        return L[0] == e
    elif L[0] ==e:
        return True
    else:
        return in_list(L[1:], e)

L = [1,5,6,7,8,5,4,2]
e = 8
print(in_list(L, e))
