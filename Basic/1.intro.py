print('Hello World')

"""
Lets start with PYTHON DATATYPES

There are Two Type of data Types in Python 

1. Mutable (List, Dict, Set):
Mutable are those whose memory address can be muted which means we can update record in it and thier memeory address remains same(muted)
For Exmple:
We can perform update, delete, add in List, Dict and Sets record, their each index value is changeable.
In mutable List is ordered which means in List data is created in an order while Dict and set don't follow this rule.

2. Immutable (Int, Float, Bool, Str, Tuple):
Immutable are those whose memory address cannot be muted which means we can not update record in it and thier memeory address changes when we do so.
For Exmple:
When We update Int, Float or Bool value it destroy the previous address and creates a new address for it.
In terms of str we only concat or extend but dont update the original string, so ultimately a new address is created for updated one.
Tuple keeps data in ordered format and we can also not update it, rather can concat it by creating a new one and ultimately its address will be created new.
"""


"""Immutable Data Types"""

# Integers
num1 = int(input("Enter Number One: "))
num2 = int(input("Enter Number Two: "))
sum = num1 + num2
print(f"Sum of {num1} and {num2} = ",sum)


# Float
float1 = float(input("Enter Float One: "))
float2 = float(input("Enter Float Two: "))
float_sum = float1 + float2
print(f"Float Sum of {float1} and {float2} = ",float_sum)


# Bool
is_sum =True
print(is_sum)
is_sum =False
print(is_sum)


# Strings
str1 = input("What's your name: ")
print("Your name is: ",str1)
i = str1[2]             # We can get specific index of string
# str1[2] = 's'         #(we cannot update in strings)
print(i)


# Tuples
tuple1 = (1,2,3,4,5)
print(type(tuple1))
for i in range(len(tuple1)):
    print(tuple1[i])
# tuple1[1] = 2         # 'Tuple' object does not support item assignment
print(tuple1)



""" Mutable data Types"""

# List
list1 = [1, 2, 3, 4, 5, 'ocman']
print(list1)
list1[2] = 1
print(list1)
list1.append("nazir")
print(list1)
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print(list1)


# Dictionary
dict1 = {'Pakistan':'Islamabad', 'India':'New Delhi', 'China':'Bejing'}

for key,value in dict1.items():
    print(key, '--', value)

dict1['Afghanistan'] = 'Bejing'
print(dict1)
dict1['Pakistan'] = 'Islamabadd'
print(dict1)
del dict1['India']
print(dict1)


# Sets
set1 = {1,2,3,4,5}
print(set1)
set1.add(1)         # As it is already in set, so it will not be added.
set1.add(6)
print(set1)
set1.remove(6)
print(set1)


# Typecasting
typecast_num = input("Enter Integer")
print(type(typecast_num))
typecast_num = float(typecast_num) 
print(type(typecast_num))
typecast_num = int(typecast_num) 
print(type(typecast_num))
