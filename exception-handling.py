# Exception Handling
# 41. Apply exception handler code in the above usecase number 35 to achieve the followings
# a.  If the calculator function is called with either the first or second argument as non integer values
# then raise Exception and call the calculator function with the type casted value
# for eg. calc("10",20, "add") in the except block of the exception handler
# we have to call the same function as calc(int("10"),20, "add") and return the result to the calling environment.
def calculator_excp(operand1, operand2, operation='add'):
    try:
        if (not isinstance(operand1, int)) or (not isinstance(operand2, int)):
            raise TypeError("Only integers are allowed")
    except:
        # print("One of the operands is non integer")
        return calculator_excp(int(operand1), int(operand2), operation)
    else:
        if (operation == 'add'):
            return  operand1 + operand2
        elif (operation == 'sub'):
            return operand1 - operand2
        elif (operation == 'div'):
            return  operand1 / operand2
        elif (operation == 'mul'):
            return  operand1 * operand2
        elif (operation == 'all'):
            return  operand1 + operand2, operand1 - operand2, operand1 * operand2, operand1 / operand2

if __name__ == '__main__':
    print(calculator_excp('10', 20, 'mul'))
    print(calculator_excp(10, '20'))
    print(calculator_excp('10', '3', 'all'))

