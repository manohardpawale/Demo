fhand=open('romeo.txt')
t=[]

for i in fhand:
    w=i.split()
    for z in range(len(w)):
        if w[z] in t:
            continue
        else:
            t.append(w[z])
t.sort()
print(t)
    