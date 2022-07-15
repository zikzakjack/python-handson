# 1. Create 2 variables with x as 100 & y as 10 respectively and find the Multiplication and division of both and store in some val as z and z1.
x = 100
y = 10
z = x * y
z1 = x / y
print('x * y = ' + str(z))
print('x / y = ' + str(z1))


# 2. Create a as 2000 and find the division of a by y (created in step 1) and reassign a with the divided result (200).
a = 2000
ay = a / y
a = ay
print('a / y = ' + str(a))


# 3. Prove Python is Dynamically Typed Language: Create x:int=100, then assign the x to y,
# but the datatype of y has to be of type string. (think about using some function like str()).
# Print the type of y and x
x: int = 100
yy: str = "hi"
print('Before Assignment -> type(x) : ' + str(type(x)) + ' & type(yy) : ' + str(type(yy)))
yy = x
print('After Assignment -> type(x) : ' + str(type(x)) + ' & type(yy) : ' + str(type(yy)))


# 4. Prove Python has dynamic inference feature
price = 500.99
print('DataType of price is dynamically inferred as ' + str(type(price)))


# 5. Prove Python is Strongly Typed Language
items = '5'
# total = price * items
"""
 above line will not work as datatype of items is inferred as string.
 TypeError: can't multiply sequence by non-int of type 'float'
"""
print('Strong typing indicates that the type matters when performing operations on a variable. ')


# 6. Create variables a,b,c,d assigned with 10,20,30,40 respectively
a, b, c, d = 10, 20, 30, 40
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('d = ' + str(d))


# 7. Prove Python variables are case sensitive
PRICE = ' its a costly deal'
print('price and PRICE are different -> type(price) : ' + str(type(price)) + ' & type(PRICE) : ' + str(type(PRICE)))


# 8. Prove variable name can’t start with numbers or cannot contains special character other than _

# 1var = 'one'
# var! = 'one'
# var@ = 'one'
# var# = 'one'
# var$ = 'one'
# var% = 'one'
# var^ = 'one'
# var& = 'one'
# var* = 'one'
# var( = 'one'
# var) = 'one'
# var- = 'one'
# var+ = 'one'
# Above variables are invalid because of special characters and numbers. only _ is allowed
var_ = 'one'
_var = 'one'
print('var_ = ' + var_ + ' _var = ' + _var)


# 9. Show some examples of when do we use single, double and triple (single/double) quotes
mystringliteral1 = "this is a string with 'quotes'"
mystringliteral2 = 'this is a string with "quotes"'
mystringliteral3 = """this is a string with "quotes" and more 'quotes'"""
mystringliteral4 = '''this is a string with 'quotes' and more "quotes"'''
mystringliteral5 = 'this is a string with \"quotes\"'
mystringliteral6 = 'this is a string with \042quotes\042'
mystringliteral7 = 'this is a string with \047quotes\047'

print(mystringliteral1)
print(mystringliteral2)
print(mystringliteral3)
print(mystringliteral4)
print(mystringliteral5)
print(mystringliteral6)
print(mystringliteral7)


# 10. Show an examples to use arithmetic, comparison, relational and logical operators.
print('Python Arithmetic Operators')
print('a + b = ' + str(a + b))
print('a - b = ' + str(a - b))
print('a * b = ' + str(a * b))
print('a / b = ' + str(a / b))
print('a % b = ' + str(a % b))
print('a ** b = ' + str(a ** b))
print('a // b = ' + str(a // b))

print('Python Comparison Operators')
print('a == b = ' + str(a == b))
print('a != b = ' + str(a != b))
print('a > b = ' + str(a > b))
print('a >= b = ' + str(a >= b))
print('a < b = ' + str(a < b))
print('a <= b = ' + str(a <= b))

print('Python Logical Operators')
print('a > 5 and a < 10 ' + str(a > 5 and a < 10))
print('a > 5 or a < 10 ' + str(a > 5 or a < 10))
print('not(a > 5 and a < 10) ' + str(not (a > 5 and a < 10)))


# 11. Write a program to find the greatest of 3 numbers
print('Write a program to find the greatest of 3 numbers')
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a >= b) and (a >= c):
    greatest = a
elif (b >= a) and (b >= c):
    greatest = b
else:
    greatest = c
print("The largest number is", greatest)


# 12. Write a single program to find the given number is even or whether it is negative
# and print the output as (the given number is even but not negative or the given number is not even
# but negative or the given number is neither negative nor even)
print('Write a program to find the given number is even or whether it is negative')
num = int(input("Enter a number: "))
if ((num % 2) == 0) and (num > 0):
    print('the given number is even but not negative')
elif ((num % 2) != 0) and (num < 0):
    print('the given number is not even but negative')
else:
    print('the given number is neither negative nor even')


# 13. Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000,
# if student choosing spark then fees is 15000, if the student choosing datascience then check if machinelearning then 25000 or
# if deep learning then 45000 otherwise if both then 25000+25000.
course = input("Which course are you enrolling (bigdata | spark | datascience )")
if (course == 'bigdata'):
    fees = 25000
elif (course == 'spark'):
    fees = 15000
elif (course == 'datascience'):
    specilisation = input("choose datascience specilisation (machinelearning | deeplearning | both)")
    if (specilisation == 'machinelearning'):
        fees = 25000
    elif (specilisation == 'deeplearning'):
        fees = 45000
    elif (specilisation == 'both'):
        fees = 25000 + 25000
print(course + ' Course fees is ' + str(fees))


# 14. Check whether the given string is palindrome or not (try to use some function like reverse).
# For eg: x="madam" and y=”madam”, if x matches with y then print as "palindrome" else "not a  palindrome".
print("palindrome check")
word = input("Enter a word...")
reversedWord = word[::-1]
if word == reversedWord:
    print(word + ' is a palindrome.')
else:
    print(word + ' is not a palindrome.')


# 15. Check whether the val x=100 is an integer or string.
# (try to use some functions like str or upper function etc to execute this use case)
# or use isinstanceof(variablename,datatype) function.
newWord = "hello guys"
if isinstance(newWord, str):
    print(newWord.upper())
else:
    print(newWord + 10)


# 16. Create a list with a range of 10 values starting from 2 to 11 and prove mutability by updating the
# 3rd element with 100 and prove resizable properties by adding 100 in the 5th position.

nos = list(range(2,12))
print(nos)
nos[2] = 100
nos.insert(4, 100)
print(nos)


# 17. Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","Ltd"),
# prove immutability and non resizable nature, access the 2nd and 4th fields and store in another tuple.

tup = ("Inceptez","Technologies","Pvt","Ltd")
## Immutable. Below assignment wont work
# tup[1] = "Consultancy"
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created. Below line wont work
# tup.__add__("hi")
new_tup = tuple((tup[1], tup[3]))
print(tup)
print(new_tup)


# 18. Convert the list of tuples [("Inceptez","Technologies"),("Apple","Incorporation")] to list of dictionary type,
# using for loop as given below [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] ,
# once the list of dictionary is arrived print only "Incorporation" by passing "Apple" as a key using dict["Apple"]
# and dict.get("Apple") and try with dict["Apple1"] and dict.get("Apple1") then find the difference between get and using[] notation.

tuples_list = [("Inceptez", "Technologies"), ("Apple", "Incorporation")]
print(tuples_list)
dicts_list = []
for tup in tuples_list:
    print(tup)
    dict_item = {}
    dict_item[tup[0]] = tup[1]
    dicts_list.append(dict_item)
print(dicts_list)


# 19. Create a list of tuple as given below and delete all duplicate tuples of the list
# lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]

lst = [("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
print(lst)
set = set()
set.update(lst)
print(set)


# 20. Append ("Intel","Corp") in the above de duplicated list

set.add( ("Intel","Corp"))
print(set)


# 21. Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] to lst1=["Inceptez","Apple"] ,
# think about using for loop, list() function, keys function and list append functions to achieve this.

lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
print(lst_dict)
lst_keys = []

for dict in lst_dict:
    for dict_key in dict.keys():
        lst_keys.append(dict_key)
print(lst_keys)


# 22. Create a list of values lst=[10,20,40,30,20], find the first, last values of the list,
# sort the list in ascending order, sort in descending order,
# print the minumum and maximum values of the descending sorted list,
# find the sum of all elements in the list, remove the number 30 and 20 from the list.

lst=[10,20,40,30,20]
print("length of the list = " + str(len(lst)))
print("first value = " + str(lst[0]))
print("first value = " + str(lst[len(lst) -1]))
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)
print("min value in the list = " + str(min(lst)))
print("max value in the list = " + str(max(lst)))
print("sum of  the list = " + str(sum(lst)))
lst.remove(30)
print(lst)
lst.remove(20)
print(lst)


# 23. Do the above same (step 22) operation in the tuple of elements tup=(10,20,40,30,20)

tup = (10, 20, 40, 30, 20)
print("length of the list = " + str(len(tup)))
print("first value = " + str(tup[0]))
print("first value = " + str(tup[len(tup) - 1]))
tup = tuple(sorted(tup))
print(tup)
tup = tuple(sorted(tup, reverse=True))
print(tup)
print("min value in the list = " + str(min(tup)))
print("max value in the list = " + str(max(tup)))
print("sum of  the list = " + str(sum(tup)))
lst = list(tup)
lst.remove(30)
tup = tuple(lst)
print(tup)
lst = list(tup)
lst.remove(20)
tup = tuple(lst)
print(tup)


# 24. Convert the string to list from str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']

str1="Inceptez Technologies Pvt Ltd"
print(str1)
lst_str1 = str1.split(" ")
print(lst_str1)


# 25. With the below given data in the format of list(list(elements))
# emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
#
# Display the below output for all of the 5 given simple scenarios
# a. Convert the first element of the above list into tuple
# ("1", ("Arun","Kumar"), "10000")
# b. Print the second element's second element and reverse the first and last name as given below
# ("Mohan","Bala")
# c. Convert the emplstlst into tuples(tuples)
# emplstlst= (("1", ("Arun","Kumar"), "10000"),("2", ("Bala","Mohan"), "12000"))
# d. Add all salary of the above list
# 22000

emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
print(emplstlst)
# a. Convert the first element of the above list into tuple
for emplst in emplstlst:
    tup = tuple(emplst)
    print(tup)

# b. Print the second element's second element and reverse the first and last name as given below
for emplst in emplstlst:
    tup = tuple(emplst)
    print(tuple([emplst[1][1], emplst[1][0]]))

# c. Convert the emplstlst into tuples(tuples)
tuplesList = []
tuplesOfTuples = tuple()
for emplst in emplstlst:
    tup = tuple(emplst)
    tuplesList.append(tup)
print(tuple(tuplesList))

# d. Add all salary of the above list
total_sal = 0
for emplst in emplstlst:
    total_sal = total_sal + int(emplst[2])
print(total_sal)


# Control Statements

# 26. Write a program using for loop to print even numbers and odd numbers in the below range of data
# (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

nos = range(5, 21)
even_lst = []
odd_lst = []
for no in nos:
    if (no % 2 == 0):
        even_lst.append(no)
    else:
        odd_lst.append(no)
print('even nos : ' + str(even_lst))
print('odd nos : ' + str(odd_lst))


# 27. Write a while loop to loop from 0 till 21 with the increment of 3,
# the result should be exactly 3,6,9,12,15,18 and store this result in a list

num_list = []
num = 0
while (num < 21):
    num = num + 3
    num_list.append(num)
    if (num >= 18):
        break
print(num_list)


# 28. Write a for or while loop to print the cube of 4, result should be 4*4*4=64
# (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)

no = 4
result = 1
for counter in range(1, 4):
    result = result * no
print(result)


# 29. Create a list as sal_lst=[10000,20000,30000,10000,15000],
# loop through the list and add 1000 bonus to the salary and
# store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
# then store the bonus applied salary in another list where sal>11000

sal_lst = [10000, 20000, 30000, 10000, 15000]
sal_bon_lst = []
sal_bon_filter_lst = []
bonus = 1000
for sal in sal_lst:
    new_sal = bonus + sal
    sal_bon_lst.append(new_sal)
    if (new_sal > 11000):
        sal_bon_filter_lst.append(new_sal)
print(sal_bon_lst)
print(sal_bon_filter_lst)


# 30. Write a do while loop to print “Inceptez technologies” n number of times as per the input you get from the user.
# Minimum it has to be printed at least one time regardless of the user input.

counter = 1
ip = input("Enter no of times : ")
if (int(ip) > 1):
    counter = int(ip)
while (counter >= 1):
    print("Inceptez technologies")
    counter = counter -1


# 31. From the given list of list of elements produce the following output using nested for loop
# lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and the max value of all the elements in the lst1.

full_list = []
lst1=[[10,20],[30,40,50],[60,70,80]]
for list in lst1:
    for item in list:
        full_list.append(item)
print(full_list)
print("min value in the list = " + str(min(full_list)))
print("max value in the list = " + str(max(full_list)))
print("sum of  the list = " + str(sum(full_list)))


# 32. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# .
# .
# 10 x 3 = 30

for no in range(1, 11):
    result = no * 3
    print(f"{no} x 3 = {result}")


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
