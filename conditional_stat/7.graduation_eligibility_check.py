gpa = float(input("Enter GPA: "))
credits = int(input("Enter the credits: "))
exam = input("Enter if final exam passed (true/false): ")

if gpa >= 2.5 and credits >= 120:
    print("Eligible")
else:
    print("Not Eligible")    

if gpa < 3.0:
    if exam == "true":
        print("Eligible")
    elif exam == "false":
        print("Not Eligible")
    else:
        print("Invalid input for exam result.")



    
