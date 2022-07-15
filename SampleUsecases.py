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
fees = -1
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


if __name__ == '__main__':
    print('hi')

