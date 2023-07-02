word='brontosaurus'
d=dict()
for c in word:
    # Use get() method alternative
    #d[c]=d.get(c,0)+1
    if c not in d:
        d[c]=1
        #print('Enter key')
    else:
        #print('Increment', print(d[c]))
        d[c]=d[c]+1
print(d)
print(d.get('u',0))
print(d.get('x',0))