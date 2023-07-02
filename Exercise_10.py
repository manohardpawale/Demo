total=0
count=0

while True:
      n=input("Enter Number or Done!")
      
      try:
            n=float(n)
            total=total+n
            count=count+1
      except:
            if n=="Done!" or n=="done":
                print("Done!")
                break
            else:
                print("Invalid Input")

print("Total:",total)
print("Count",count)
print("Avarage:",total/count)