fhand=open('mbox-short.txt')

count=0

for i in fhand:
    j=i.split()
    
    if len(j)==0: continue
    if j[0]=='From':
        count+=1
        print(j[1])
print('There were %d lines in the file with Form as the first word' %count)