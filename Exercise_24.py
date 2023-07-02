import string
fname=input('Enter File Name: ')
d=dict()
lst=list()
try:
    fhand=open(fname)
except:
    print('Enter Valid File Name')
    exit()

for line in fhand:
    line=line.strip()
    line=line.translate(str.maketrans('','',string.punctuation))
    words=line.split()

    for i in words:
        d[i]=d.get(i,0)+1
        '''
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
        '''
    
keys=None
values=None
for k,v in d.items():
    if values is None or v>values:
        keys=k
        values=v
print(keys,':',values)