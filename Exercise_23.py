fhand=open('romeo.txt')
d=dict()

for n in fhand:
    w=n.split()
    for i in w:
        d[i]=d.get(i,0)+1
print(d)
