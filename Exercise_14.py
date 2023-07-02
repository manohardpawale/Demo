lx=list()
while True:
    x=input('Enter Number: ')
    if x=='done':break
    try:
        x=float(x)
    except:
        print("Enter Valid Number")
        continue
    lx.append(x)
print(sum(lx)/len(lx))
