fhand=open('words.txt')
#print(fhand)
#t=[]
g=dict()
for line in fhand:
    words=line.split()
    for i in words:
        if i not in g:
            g[i]=1
        else:
            g[i]=g[i]+1
        #t.append(i)
print(g)