#CALCULATOR PRODUCT

def calculator():
    print("Welcome to Calculator ")
    print("ENJOY USING OUR PRODUCT")
    print("use only this signs + - * /")
    
    operator = input("Which operation do you want to carry(+,-,*,/): ")
    num1 = int(input("Enter first value: ")) #int is used here to cast the input to integers
    num2 = int(input("Enter second Number: "))
    
    if operator == "+":
        print(f"The sum of {num1} and {num2} is: ",num1 + num2)
    elif operator == "-":
        print(f" the difference of {num1} an {num2} is: ",num1 - num2)
    elif operator == "*":
        print(f"the product of {num1} and {num2} is: ",num1*num2)
    elif operator == "/":
        if num2 != 0:
            print(f"the division of {num1} by {num2} is: ",num1/num2)
        else:
            print("The second number cannot be zero")
            print("PLease verify")
    
calculator()