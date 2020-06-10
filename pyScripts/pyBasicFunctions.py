# Return multiple Values
def generate_list(name, num_elements=2):  # 2 as default value for num_elements argument
    return [name for _ in range(num_elements)]  # comprehension in return statements


some_list = generate_list("techecoder", 5)  # Function calling using Positional arguments
another_list = generate_list("github", num_elements=6)  # Keyword arg should always followed by Positional arg
print(type(some_list))  # type of return should be list, Default return in python is always NONE
print(some_list)  # print tuple of names
print(another_list)


# functions with variable arguments,
def students_in_college(college, city1, *students):
    print("My name is", college)
    print("my college name is: ", city1)
    print("The students enrolled are:", students)


list12 = ["Techie", "Coder"]
students_in_college("IIT", "India", "Techie", "Coder")
students_in_college("IIT", "India", *list12)  # We have to add * if passing list as students.


# Function calling multiple Keyword arguments
def student_details(**details):
    for key, value in details.items():
        print(key, value)


detail_dict = {'name': "teche", 'age': 18, 'college': "boston university"}
student_details(**detail_dict)  # We have to add ** if passing dict as arguments.


# function to call both variable positional and keyword arguments
def student_in_college(*student_detail, **college):
    print("Students--")
    for i in student_detail:
        print(i)
    print()
    print("College Details--")
    for key, value in college.items():
        print(key, value)


student_in_college("Alison", "Bob", "Charlie", name="stanford", city="LA")  # Calling both positional and Keyword args


# Function to return multiple values
def add_sub(x, y):
    add_results = x + y
    sub_results = x - y
    return add_results, sub_results


tuple13 = add_sub(6, 5)  # return as tuple
result_1, result2 = add_sub(8, 4)
a, _ = add_sub(9, 2)  # Put _ if second return value not being used
print(tuple13, result_1, result2, a)

# Global and local variables in function
country = "USA"  # Global variable
city = "Seattle"  # Global variable


def some_fn():
    country1 = "India"  # Local variable override global variable
    global city  # define city as global variable in case same name local variable exist in function
    city = city + "-City"  # defining local city variable using Global city variable
    print("Country: ", country1)  # Local value override here and print "India"
    print("City: ", city)  # Global variable value Seattle print here


some_fn()
# Function Argument passing by value: Impact on only inner print
fruit_list = ["Apple", "Banana"]  # Define Global variable


def change_list1(fruit_list):
    fruit_list = ["Mango", "Banana"]  # Define new local list
    print("Inside the function passing by value: ", fruit_list)  # This will print updated list


change_list1(fruit_list)
print("Outside the function passing by value: ", fruit_list)  # Print global list values only


# Function Argument passing by Reference: Update global List as well.
def change_list2(fruit_list):
    fruit_list[1] = "Kiwi"
    fruit_list.append("grapes")
    print("Inside the function passing by Reference: ", fruit_list)


change_list2(fruit_list)
print("Outside the function passing by Reference: ",
      fruit_list)  # Print updated List as Global list has been modified in function

# help("modules") this will give all python modules installed in pycharm
