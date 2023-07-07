a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

while(True): 
    print("1.Add 2. Subtract 3.Multiply 4.Divide")
    n=int(input("Enter your choice: "))
    
    if (n==1):
        ans=a+b
        print("Answer: ",ans)
    elif (n==2):
        if (a>b):
            ans=a-b
            print("Answer: ",ans)
        else:
            ans=b-a
            print("Answer: ",ans)
    elif (n==3):
        ans=a*b
        print("Answer: ",ans)
    elif (n==4):
        ans=a/b
        print("Answer: ",ans)
    else:
        break
