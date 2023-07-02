def compute_pay(hours,rate):
    pay=hours*rate
    return pay
    
def receive_input():
    hrs=input("Enter Hours: ")
    rt=input("Enter Rate: ")
    return (hrs,rt)

def display_pay(val):
    print("Your Pay is: ",val)
    
x=receive_input()
    
x1=float(x[0])
x2=float(x[1])

y=compute_pay(x1,x2)

display_pay(y)