def perform_operation(num1:float, num2:float, operation:str):
#  while(operation == 'add' or operation == 'multiply' or operation == 'subtract' or operation == 'divide'):
    if(operation == 'add'):
        return num1 + num2
    elif (operation == 'multiply'):
        return num1 * num2
    elif (operation == 'subtract'):
        return num1 - num2
    elif (operation == 'divide'):
        if(num2 == 0):
            print( '∞')
        else:
            return num1/num2
    else:
        print("Operation must be only: 'add', 'subtract', 'multiply','divide'") 
    