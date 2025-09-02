student_data={}
while True:
    print("1. Add Student ","2. Edit Student Info","3. Delete Student","4. View All","5. Search","6. Exit",sep="\n")
    choice = int(input("Enter your choice "))
    match choice:
        case 1:
            roll_no=int(input("Please enter roll no ")) 
            name = input("Please enter name")
            student_data[roll_no]=name
        case 2:
            pass
        case 3:
            pass
        case 4:
            print(student_data)
        case 5:
            pass
        case 6:
            break
        