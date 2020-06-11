# return function from another function
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def get_function(operator='+'):  # This function will return another function based on input argument
    if operator == '+':
        return add
    elif operator == '-':
        return sub
    else:
        return None


func = get_function('+')
print(func)  # Return function 'add'
result131 = func(3, 4)  # add function will be called on arguments
print(result131)
calc_dict = {'+': add, '-': sub}  # Define Dict for operator and functions defined above
func1 = calc_dict['-']  # Calling Dict to assign function based on input
result321 = func1(6, 2)
print(result321)
result1234 = calc_dict['+'](100, 400)  # Another way to call function based on Dict Key
print(result1234)

# Define, Invoke and Discard Lambda function in python
# Lambda function syntax is x = (lambda <args>: <expression>)(args value)
# Lambda function can only have expression, does not support complex statement i.e. ifelse or loops
sum1 = (lambda *args: sum(args))(3, 4, 5, 6)  # Passing multiple arguments in lambda and invoking in same command
print(sum1)
sum2 = (lambda **num_dict: sum(num_dict.values()))(a=23, b=34, c=45)  # Passing dictionary in lambda and invoking
# in same command
print(sum2)

# Lambda filter function in python
num_list12 = [1, 4, 6, 3, 10, 14, 16, 18]
even_list = list(
    filter(lambda x: x % 2 == 0, num_list12))  # lambda filter function return filter object, hence converted into list
print(even_list)


# Recursive Functions: Calling same function within function
# This function with print all values until num=0
def decrement(num):
    if num == 0:
        return
    print(num, end=" ")
    decrement(num - 1)


decrement(10)
print()


# Recursive function Fibonacci series
def fibonacci(number, fi_series):
    if number == 2:
        return
    l = len(fi_series)
    new_number = fi_series[l - 1] + fi_series[l - 2]
    fi_series.append(new_number)
    print("series so far: ", fi_series)
    fibonacci(number - 1, fi_series)


f_series = [0, 1]
fibonacci(10, f_series)
print(f_series)


# Python Generators are used to generate sequence using yield command
def gen_sqr(limit):
    for i in range(0, limit):
        yield i ** 2


g = gen_sqr(10)
print(next(g))  # generator can be called using next command
g_list = list(gen_sqr(12))  # assign all next values in list
print(type(g))
print(g_list)

# Closure: A function defined within another function
import random


def greet_message(name, message):
    annotation = ['-', '*', '+', '^', '~']
    annotate = random.choice(annotation)

    def greetings():
        print(annotate * 50)
        print(message, name)
        print(annotate * 50)

    return greetings


# calling greet_message functions here
greet_greg_fn = greet_message('Hello', 'Greg')
greet_claudia_fn = greet_message('Good Morning', 'Claudia')
greet_jon_fn = greet_message('Hey! ', 'Jon')
greet_jon_fn()
greet_claudia_fn()
greet_greg_fn()

# Another example of closure where multiple students are enrolling in different universities
def enroll_in_college(college_name):
    student_list = []
    def enroll_student(student_name):
        student_list.append(student_name)
        print("Student", student_name, "has benn enrolled in ", college_name)
        print("Current Students ", student_list, end="\n\n")
    return enroll_student

# Call enroll_in_college function for each college
enroll_in_yale_fn = enroll_in_college('Yale')
enroll_in_duke_fn = enroll_in_college('Duke')
# Call above college function to enroll students in each university
enroll_in_yale_fn('Sam')
enroll_in_duke_fn('Robert')

# Function Decorator examples: These decorators can be used in common error handling
def make_highligter(func):
    annotations = ['-', '*', '+', '^', '~']
    annotates = random.choice(annotations)

    def highlight():
        print(annotates * 50)
        func()
        print(annotates * 50)
    return highlight

# Calling above decorator function before defining function argument
@make_highligter
def print_message():
    print("How are you!!")

@make_highligter
def print_message2():
    print("Good Morning!!")

print_message()  # Calling function
print_message2()  # Calling function




