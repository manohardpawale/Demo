max=None
min=None

while True:
      n=input("Enter Number or Done!")
      try:
        n=float(n)
        if max is None or max<n:
            max=n
        if min is None or min>n:
            min=n
      except:
        if n=="Done!" or n=="done":
            print("Done!")
            break
        else:
            print("Invalid Input")
print("Max:",max)
print("Min",min)