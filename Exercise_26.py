fhand=open('mbox-short.txt')
dmail=dict()

for line in fhand:
    if not line.startswith('From '): continue
    line=line.split()
    if len(line)<1:continue
    dmail[line[1]]=dmail.get(line[1],0)+1

mostmail=None
mostid=None
for m, c in dmail.items(): 
    if mostmail is None or c>mostmail:
        mostmail=c
        mostid=m
print(mostid,mostmail)