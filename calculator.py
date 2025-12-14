Number1=int(input("Enter the frist number is: "))
Number2=int(input("Enter the second number is: "))

operation=input("Enter your operation:" )
add= Number1+Number2
sub= Number1-Number2
mul= Number1*Number2
divide= Number1/Number2

if(operation== '+' or operation=='-' or operation=='*' or operation=='/'):
    if (operation== '+' ):
        print("The sum of", Number1 ,"and" ,Number2, "is:", add)

    elif (operation== '-' ):
        print("The substraction of", Number1 ,"and" ,Number2, "is:", sub)

    elif (operation== '*' ):
        print("The multification of", Number1 ,"and" ,Number2, "is:", mul)

    elif (operation== '/' ):
        print("The divition of", Number1 ,"and" ,Number2, "is:", divide)
else:
    print("Enter only one valid operation")