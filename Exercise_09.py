def compute_grade(score):
    if s>1 or s<0:
        print("Bad Score")
    else:
        if score>=0.9:
         print("Your grade is: A")
        elif score>=0.8:
         print("Your grade is: B")
        elif score>=0.7:
          print("Your grade is: C")
        elif score>=0.6:
          print("Your grade is: D")
        elif score<0.9:
         print("Your grade is: F")
    
def recive_score():
    try:
        x=input("Enter your score: ")
    except:
        print("Bad Score")

    return float(x)


s=recive_score()
compute_grade(s)