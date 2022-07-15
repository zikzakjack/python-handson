## Collections: List, Dictionary, Tuple and Set

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

