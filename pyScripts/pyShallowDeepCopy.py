# This python script will describe shallow or Deep Copy functions on string, List, Tuple and Dict
import copy

# String Operations, Strings are immutable and both Shallow and Deep copy behave in same way.
# This applies to Tuple as well
# Shallow copy operations on String
old_str = "Python"
new_str = old_str  # Shallow Copy of string
print("ShallowCopy Before: ", old_str, new_str)
old_str = 'Hello'  # Strings are immutable hence does not support item assignment.
print("ShallowCopy After: ", old_str, new_str)
# Deep copy operations on String
first_str = "John"
second_str = copy.copy(first_str)  # Copy of string
third_str = copy.deepcopy(first_str)  # Copy of string
print("Deep Copy Before: ", first_str, second_str, third_str)
first_str = 'Snow'  # Strings are immutable hence does not support item assignment.
print("Deep Copy After: ", first_str, second_str, third_str)
# List Operations
# List Shallow Copy operations
old_list = ["Jon", "Vicky", "Tom", "Aish"]
new_list = old_list  # Shallow Copy of List
print("ShallowCopy Before: ", old_list, new_list)
old_list[3] = 'Wright'  # List are mutable
print("ShallowCopy After: ", old_list, new_list)  # Both lists should show changed index value in shallow copy
# List Deep Copy operations
first_list = ["Tony", ["Jon", "Vicky"], ["Tom", "Aish"]]  # Nester list
second_list = copy.copy(first_list)  # Copy will create deep copy in outer list only
third_list = copy.deepcopy(first_list)  # Deep copy will create Deep copy in both inner and outer lists.
fourth_list = first_list[:]  # This syntax will also create deep copy of list
print("DeepCopy Before: ", "First_List: ", first_list, "Second_List: ", second_list, "Third_List: ", third_list)
first_list[1][1] = 'Wright'  # List are mutable
first_list[0] = "Robert"
print("Copy After: ", "First_List: ", first_list, "Second_List: ",
      second_list)  # Copy command performs deep copy at outer layer only
print("DeepCopy After: ", "First_List: ", first_list, "Third_List: ",
      third_list)  # Deep Copy will do deep copy at both inner and puter layers
# Above Shallow and Deep Rules will be applied to Dict as well. The Conclusion is that String and Tuple will behave
# same in Shallow and Deep copy whereas List and Dict will behave in similar way.
