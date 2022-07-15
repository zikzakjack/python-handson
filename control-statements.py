
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

