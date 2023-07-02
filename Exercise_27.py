fhand=open('mbox-short.txt')
ddomain=dict()

for line in fhand:
    line=line.strip()
    if not line.startswith('From'): continue
    atpos=line.find('@')  
    sppos=line.find(' ',atpos)
    d=(line[atpos+1:sppos])
    ddomain[d]=ddomain.get(d,0)+1

print(ddomain)