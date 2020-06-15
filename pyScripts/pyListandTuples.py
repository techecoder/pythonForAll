# List Operations
mixed_list = [1, 2.5, True, "Hello", 5]  # List can contain any values
print(mixed_list, type(mixed_list))  # Print List and type of list
print(mixed_list[0], mixed_list[-1])  # Print first/last index of list
mixed_list[4] = 9  # update list last index
mixed_list.append("newappend")  # Append List
mixed_list.extend(["newextend1", "newextend2"])  # Add multiple values in List
mixed_list2 = [99, 98]  # new list
mixed_list += [99, 98]  # concat list
mixed_list.insert(3, "newinsert")  # Insert at particular index in List
print(mixed_list)
mixed_list.remove('Hello')  # Remove values from list
print(mixed_list)
newlist = ['Maruti', 'Ford', 'Kia', 'Mahindra']  # new list declaration
newlist.sort()  # Sorting the same list
print(newlist)
newlist.reverse()  # reverse the list
print(newlist)
newlist.pop()  # Remove last index of the list
print(newlist.count('Maruti'))  # Counting no of occurrence of Maruti in List
newlist.clear()  # clear whole list
newlist = mixed_list.copy()  # Deep copy of the list, refer different list
print(newlist)
shallowlist = mixed_list  # Shallow copy of list refer to same list
print(newlist, "", shallowlist)

# Additional built in functions for list
list_num = [10, 20, 30, 40, 50, 60]
print(max(list_num), )
sortedlist = sorted(list_num)  # Create new sorted list
list_num *= 2  # Multiply list
print(list_num)
print(list_num[2:5:2])  # slicing List with step number
print(list_num[5:2:-2])  # slicing List with step number
print(any(list_num))  # Print Boolean

# Introduction to Tuple and Tuple Operations
my_tuple = (1, 2, 3, "Hello", "Python")  # Tuple initialisation
my_tuple1 = 1, 2, 3  # Tuple initialisation
nested_tuple = (1, 2, (3, 4))  # Nested tuple
a, b, c = my_tuple1  # tuple can be assigned to different variables according to length
tuplelist = (2, 3, [6, 7], (5, 6))  # Tuples can have list as well
print(type(my_tuple), my_tuple, my_tuple1[2])  # Print tuple and elements
print(a, b, c, tuplelist, tuplelist[2][1])  # Print nested list elements
int_tuple = (1, 2, 3)  # initialise integer tuple
list_tuple = list(int_tuple)  # convert a tuple in to list
set_tuple = set(int_tuple)  # convert a tuple into set
orig_tuple = tuple(list_tuple)
print(list_tuple, set_tuple, orig_tuple)  # Print List, tuple and set
# Zip operation on tuple
tuple_a, tuple_b = (1, 2, 3, 4, 5), ('a', 'b', 'c', 'd', 'e')
zipped = zip(tuple_a, tuple_b)  # zip operation will create key value pair in both tuple and list
tuple_zip = tuple(zipped)
print(tuple_zip)
tuple_x, tuple_y = zip(*tuple_zip)  # unzip key value pairs in different tuples or list
print(tuple_x, tuple_y)
# Dictionary Operations
num_list, str_list, num_tuple = [1, 2, 3], ['one', 'two', 'three'], ('ONE', 'TWO', 'THREE')
result = zip(str_list, num_tuple)
print(dict(result))  # Creating key value pair in dictionary
# Complex Data Type using Dict and Sets
fruit_qty_consumed1 = {'Banana': [50, 60, 33, 45], 'Orange': [70, 20, 70, 50],
                       'Avocado': [60, 40, 30, 20]}  # Intialise empty dictionary
print(fruit_qty_consumed1, fruit_qty_consumed1['Banana'][0])  # Print nested values based on key
fruit_qty_consumed = {'Banana': {'fri': 50, 'sat': 60, 'sun': 33}, 'Orange': {'fri': 40, 'sat': 20, 'sun': 40},
                      'Avocado': {'fri': 10, 'sat': 90, 'sun': 80}}  # define nested dictionary
print(fruit_qty_consumed, fruit_qty_consumed['Banana']['fri'])  # Print nested value based of multiple keys
print(fruit_qty_consumed1.items())  # print dict in tuple format
fruit_qty_consumed1.pop('Banana')  # Remove Key value pair from dict
print(fruit_qty_consumed1, fruit_qty_consumed1.pop('Orange'))  # pop function will return value for specific key
# Updating Dict from another dict
dict_age, new_dict_age = {'Ethan': 55, 'Sofia': 45}, {'Ethan': 65, 'Sofia': 45}
print(dict_age, new_dict_age)
dict_age.update(new_dict_age)  # Updated Ethan age in dict_age from new_dict_age
new_dict_age.clear()  # Clear dict key values and make it empty
print(dict_age, new_dict_age)
