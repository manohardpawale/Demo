fhand=open('mbox.txt')
days=dict()

for line in fhand:
    line=line.strip()
    if not line.startswith('From'): continue
    words=line.split()
    
    if len(words)<3:continue
    d=words[2]
    days[d]=days.get(d,0)+1
print(days)