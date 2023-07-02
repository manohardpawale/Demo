fname=input('Enter File Name: ')
try:
    fhand=open(fname)
except:
    print('Enter Valid file Name')
    exit()
count=0
scon=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('X-DSPAM-Confidence'): continue
    xpos=line.find(':')
    fnum=float(line[xpos+1:].strip())
    scon=scon+fnum
    count=count+1
    #print(fnum)
print('Spam Confidence:',scon)
print('Count:',count)
print('Avarage Spam Confidence:',scon/count)