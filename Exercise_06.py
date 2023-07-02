hours=input("Enter Hours: ")
rate=input("Enter Rate: ")

try:
    hours=float(hours)
    rate=float(rate)
except:
    print("Error!,\nPlase eneter value in numeric")

pay=hours*rate
print ("pay: ", pay)