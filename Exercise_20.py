t=[]

while True:
    urinp=input('Enter Number: ')
    if urinp=='done':
        break
    else:
        try:
            urinp=float(urinp)
        except:
            print('Enter Valid Number')
            continue
    t.append(urinp)

if len(t)==0:
    print('------Program End-------')
else:
    print(max(t))
    print(min(t))