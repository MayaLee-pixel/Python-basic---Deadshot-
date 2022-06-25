# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print("#1")
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e), "\n")

# 2. Append 4 and 5 to the lst_d and define the id one more time
print("#2")
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d), "\n")

# 3. Define the type of each object from step 1.

print("#3")
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e), "\n")

# 4*. Check the type of the objects by using isinstance
print("#4")
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict), "\n")

 # String formatting:
 # Replace the placeholders with a value:
 # "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("#5")
print("Anna has {} apples and {} peaches.".format(12, 6), "\n")

# 6. By passing index numbers into the curly braces
print("#6")
print("Anna has {0} apples and {1} peaches.".format(11, 5), "\n")

# 7. By using keyword arguments into the curly braces.
print("#7")
print("Anna has {apl} apples and {pch} peaches.".format(apl=10, pch=4), "\n")

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("#8")
print("Anna has {0:5} apples and {1:3} peaches.".format(9, 3), "\n")

# 9. With f-strings and variables
print("#9")
a = 8
p = 2
print(f"Anna has {a} apples and {p} peaches.", "\n")

# 10. With % operator
print("#10")
a_number = 7
p_number = 1
print("Anna has %s apples and %s peaches." % (a_number, p_number), "\n")

# 11*. With variable substitutions by name (hint: by using dict)
print("#11")
a_num = 6
p_num = 0
data_dict = {"1": a_num, "2": p_num}
print("Anna has %(1)s apples and %(2)s peaches." % data_dict, "\n")

# 12. Convert (1) to list comprehension
print("#12")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print([num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)], "\n")

# 13. Convert (2) to regular for with if-else
print("#13")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension, "\n")

# 14. Convert (3) to dict comprehension.
print("14")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
print({num: num ** 2 for num in range(1, 11) if num % 2 == 1}, "\n")

# 15*. Convert (4) to dict comprehension.
print("#15")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
print({num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}, "\n")

# 16. Convert (5) to regular for with if
print("#16")
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension, "\n")

# 17*. Convert (6) to regular for with if-else.
print("#17")
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print(dict_comprehension, "\n")

# 18. Convert (7) to lambda function
print("#18")
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(7, 12))
foo = lambda x, y: x if x < y else y
print(foo(7, 12), "\n")

# 19*. Convert (8) to regular function
print("#19")
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(9, 46, 15))
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(9, 46, 15), "\n")

# 20. Sort lst_to_sort from min to max
print("#20")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(lst_to_sort)
print(sorted(lst_to_sort), "\n")

# 21. Sort lst_to_sort from max to min
print("#21")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(lst_to_sort)
print(sorted(lst_to_sort, reverse=True), "\n")

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("#22")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(lst_to_sort)
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort, "\n")

# 23*. Raise each list number to the corresponding number on another list
print("#23")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list_A)
print(list_B)
print(list(map(lambda x, y: x + y, list_A, list_B)), "\n")

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1
print("#24")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(lst_to_sort)
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)), "\n")

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("#25")
b = range(-10, 10)
print(list(filter(lambda x: x < 0, b)), "\n")

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_1, list_2)), "\n")
