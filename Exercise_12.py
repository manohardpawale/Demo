largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    
    if smallest is None or smallest>num:
        smallest=num
    
    if largest is None or largest<num:
        largest=num

print("Maximum is", largest)
print("Mininum is",smallest)