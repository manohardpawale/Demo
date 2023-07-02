fhand=open('mbox-short.txt')
count=0

for i in fhand:
    w=i.split()
    if len(w)==0 or w[0]!='From':continue
    print(w[2])
