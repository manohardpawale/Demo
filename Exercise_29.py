fname=input('Enter File Name ')

try:
    fhand=open(fname)
except:
    print('Enter Valid File Name')
    exit()

mailcount=dict()

for line in fhand:
    line=line.strip()
    if not line.startswith('From '):continue
    words=line.split()


    if words[1] not in mailcount:
        mailcount[words[1]]=1
    else:
        mailcount[words[1]]+=1

maillst=list()
for key,val in mailcount.items():
    maillst.append((val,key))

maillst.sort(reverse=True)
key,val = maillst[0]
print(val, key)
