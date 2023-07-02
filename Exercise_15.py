fhand=open('mbox-short.txt')
count=0

for i in fhand:
    i=i.strip()
    if not i.startswith('From '): continue
    count=count+1
    t=i.split()
    print(t[2])
print(count)