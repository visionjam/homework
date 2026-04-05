L=[1,2,3]
def ni(lst):
    if len(lst)==1:
        return lst
    else:
        return ni(lst[1:])+[lst[0]]
print(ni(L))