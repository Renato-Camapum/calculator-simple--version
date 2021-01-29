
from art import logo

print(logo)



def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": sub, 
    "*": mult, 
    "/": div
    }
 
def calculation():
    num1 = float(input("what is the first number: \n"))


    for symbol in operations:
        print(symbol)
    should_cont = True

    while should_cont:  
        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("what is the next number: \n"))

        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Do you want to continue 'y' or 'no'?: ") == "y":
            num1 = answer
        else:
            should_cont = False
            calculation()
            
            
calculation()