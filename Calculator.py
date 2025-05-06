

print("1 -  Addition")
print("2 -  Subtraction")
print("3 -  Multiplication")
print("4 -  Division")
print("5 -  Modulas")

Operation=int(input("choose your Operation: "))
num1=float
num2=float
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if(Operation==1):
    result= num1 + num2
elif(Operation==2):
    result =num1-num2
elif(Operation==3):
    result=num1*num2
elif(Operation==4):
    result=num1//num2
elif(Operation ==5):
    result =num1%num2
else:
    print("Invalid Operation")
print("The result of your calculation is : ", result)




    





