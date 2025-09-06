history = []
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "error: cannot divide by zero"
    return a / b 
while True :
    print("\nOptions:")
    print("1 -> Add")
    print("2 -> Subtract")
    print("3 -> Multiply")
    print("4 -> Divide")
    print("5 -> Shiw History")
    print("6 -> Exit")

    choice = input("enter your choice (1-6):")
    if choice == "6":
        print("Exiting calulator_ _ _ _")
        break
    if choice == "5":
        print("\n calculation history_ _ _ _")
        for item in history:
            print(item)
        continue 
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    if choice == "1":
        result = add(num1,num2)
        operation = f"{num1} + {num2} = {result}"
    elif choice == "2":
        result = subtract(num1,num2)
        operation = f"{num1} - {num2} = {result}"
    elif choice == "3":
        result = multiply(num1,num2)
        operation = f"{num1} * {num2} = {result}"
    elif choice == "4":
        result = divide(num1,num2)
        operation = f"{num1} / {num2} = {result}"  
    else:
        print("invalid choice ! try again")
        continue
    print("results :", result)
    history.append(operation)    


