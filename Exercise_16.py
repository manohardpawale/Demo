def chop(t):
    del t[len(t)-1]
    del t[0:1]
    return t

def middle(t):
    del t[len(t)-1]
    del t[0:1]
    return t


mylist=[1,2,3,4,5,6,7,8,9]

uplist=middle(mylist)

print(uplist)