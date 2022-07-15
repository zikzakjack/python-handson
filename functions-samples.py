
# 33. Write def functions to make the above usecases (conditional from 11 to 15 and control statements 26 to 32)
# and the upcoming usecases more generic.

def usecase11(no1, no2, no3):
    print('Write a program to find the greatest of 3 numbers')
    if (no1 >= no2) and (no1 >= no3):
        greatest = no1
    elif (no2 >= no1) and (no2 >= no3):
        greatest = no2
    else:
        greatest = no3
    print("The largest number is", greatest)


def usecase12(num):
    print('Write a program to find the given number is even or whether it is negative')
    if ((num % 2) == 0) and (num > 0):
        print('the given number is even but not negative')
    elif ((num % 2) != 0) and (num < 0):
        print('the given number is not even but negative')
    else:
        print('the given number is neither negative nor even')


def usecase13(course, specilisation = 'both'):
    fees = -1
    # course = input("Which course are you enrolling (bigdata | spark | datascience )")
    if (course == 'bigdata'):
        fees = 25000
    elif (course == 'spark'):
        fees = 15000
    elif (course == 'datascience'):
        # specilisation = input("choose datascience specilisation (machinelearning | deeplearning | both)")
        if (specilisation == 'machinelearning'):
            fees = 25000
        elif (specilisation == 'deeplearning'):
            fees = 45000
        elif (specilisation == 'both'):
            fees = 25000 + 25000
    print(course + ' Course fees is ' + str(fees))


def usecase14(word):
    print("palindrome check")
    reversedWord = word[::-1]
    if word == reversedWord:
        print(word + ' is a palindrome.')
    else:
        print(word + ' is not a palindrome.')


def usecase15(newWord):
    if isinstance(newWord, str):
        print(newWord.upper())
    else:
        print(newWord + 10)


def usecase26(start, end):
    nos = range(start, end)
    even_lst = []
    odd_lst = []
    for no in nos:
        if (no % 2 == 0):
            even_lst.append(no)
        else:
            odd_lst.append(no)
    print('even nos between ' + str(start) + ' and ' + str(end) + ' : ' + str(even_lst))
    print('odd nos between ' + str(start) + ' and ' + str(end) + ' : ' + str(odd_lst))


def usecase27(upper, incr):
    num_list = []
    num = 0
    while (num < upper):
        num = num + incr
        num_list.append(num)
    print(num_list)


def usecase28(no, pow):
    result = 1
    for counter in range(1, pow + 1):
        result = result * no
    print(result)


def usecase29(sal_lst, filter):
    sal_bon_lst = []
    sal_bon_filter_lst = []
    bonus = 1000
    for sal in sal_lst:
        new_sal = bonus + sal
        sal_bon_lst.append(new_sal)
        if (new_sal > filter):
            sal_bon_filter_lst.append(new_sal)
    print(sal_bon_lst)
    print(sal_bon_filter_lst)


def usecase30(str, ip):
    counter = 1
    if (int(ip) > 1):
        counter = int(ip)
    while (counter >= 1):
        print(str)
        counter = counter - 1


def usecase31(lst1):
    full_list = []
    for list in lst1:
        for item in list:
            full_list.append(item)
    print(full_list)
    print("min value in the list = " + str(min(full_list)))
    print("max value in the list = " + str(max(full_list)))
    print("sum of  the list = " + str(sum(full_list)))


def usecase32(times, no):
    for time in range(1, times + 1):
        result = time * no
        print(f"{time} x {no} = {result}")


# 35. Write a function to create a calculator that accepts 3 arguments
# with the datatype of first 2 as int and 3rd one is str,
# based on the 3rd argument value passed as add/sub/div/mul
# perform either addition or subraction or multiplication or division respectively of argument 1 and 2
# then return the result to the calling environment.
# Create a default argument function to handle “if the 3rd argument is not passed then default it to add”.
def calculator(operand1, operand2, operation='add'):
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


# 37. Create a method to accept a string like “inceptez technologies”
# and return the following values in multiple result types (capitalize, upper case, length of the string,
# number of words, ends with “s” or not, replace ‘e’ with ‘a’)
# for eg. the result should be like this.. (Inceptez Technologies, INCEPTEZ TECHNOLOGIES, 21, 2, True,incaptaz tachnologias)
def word_processor(input):
    upper = input.upper()
    length = len(input)
    word_count = len(input.split())
    end_with_s = input[len(input)-1] == 's'
    replace_e_with_a = input.replace('e','a')
    return input, upper, length, word_count, end_with_s, replace_e_with_a

if __name__ == '__main__':
    usecase11(10, 20, 30)
    usecase11(no3 = 40, no2 = 60, no1 = 10)
    usecase12(0)
    usecase12(-1)
    usecase12(1)
    usecase12(2)
    usecase13('spark')
    usecase14('malayalam')
    usecase14('zebra')
    usecase15(10)
    usecase15('hello guys')
    usecase26(5, 11)
    usecase27(21, 3)
    usecase28(4, 3)
    sal_lst = [10000, 20000, 30000, 10000, 15000]
    usecase29(sal_lst, 11000)
    usecase30("Inceptez technologies", 5)
    lst1 = [[10, 20], [30, 40, 50], [60, 70, 80]]
    usecase31(lst1)
    usecase32(10, 3)
    print(calculator(10, 20, 'mul'))
    print(calculator(10, 20))
    print(calculator(10, 3, 'all'))
    result = word_processor('Inceptez Technologies')
    print(result)

