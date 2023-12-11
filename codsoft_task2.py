print("\n======Calculator======")

num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))

while True:

    print("\nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division \nPress 5 to Quit\n")

    choice = int(input("Enter your choice from 1-5: "))

    if choice == 1:
        print("\n",num1,"+",num2,"=",num1+num2)
    elif choice == 2:
        print("\n",num1,"-",num2,"=",num1-num2)
    elif choice == 3:
        print("\n",num1,"x",num2,"=",num1*num2)
    elif choice == 4:
        print("\n",num1,"/",num2,"=",num1/num2)
    elif choice == 5:
        break
    else:
        print("Invalid Input")
