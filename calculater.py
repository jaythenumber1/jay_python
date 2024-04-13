
option = int(input("please select option --> 1-add,  2-sub, 3-multi, 4-div : "))
if option > 0 & option < 5 : 
    a = int(input("enter 1st number: "))
    b = int(input("enter 2nd number: "))

    #add:
    if option == 1:
        c = a + b
        print("sum of numbers: " + str(c))
    
    #sub:
    elif option == 2:
        c = a - b
        print("subtraction of of numbers: " + str(c))

    #mul:
    elif option == 3:
        c = a * b
        print("multiplication of of numbers: " + str(c))

    #div:
    elif option == 4:
        c = a / b
        print("division of of numbers: " + str(c))
else:
    print("Please select proper option")
