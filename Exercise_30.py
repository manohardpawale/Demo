fname=input('Enter File Name: ')
try:
    fhand=open(fname)
except:
    print('Enter Valid File Name')

hrscount=dict()

for line in fhand:
    line=line.strip()
    if not line.startswith('From '): continue
    words=line.split()
     
    time=words[5]

    hours=time.split(':')
    

    if hours[0] not in hrscount:
        hrscount[hours[0]]=1
    else:
        hrscount[hours[0]]+=1

hrslst=list(hrscount.items())
hrslst.sort()

for hrskey, countval in hrslst:
    print(hrskey,countval)
