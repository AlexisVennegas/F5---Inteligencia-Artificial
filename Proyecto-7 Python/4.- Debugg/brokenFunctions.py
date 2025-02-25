
def divide_numbers(a, b):
    try:
        if(b == 0):
            raise ZeroDivisionError("Error: zero division")
        result = a / b
    except ZeroDivisionError:
        result = "Error: Division by zero"
    return result


def get_element_by_index(lst, index):
    print("Index:", index)
    print("List:", lst)
    try:
        if index >= len(lst):
            raise IndexError("Error: Index out of range")
        else:
            element = lst[index]
    except IndexError:
        element = "Error: Index out of range"
    return element


def concatenate_strings(str1, str2):
    if type(str1) != str or type(str2) != str:
        try:
            str1 = str(str1)
            str2 = str(str2)
        except TypeError:
            result = "Error: Can't convert to string"
    result = str1 + str2

    return result

def print_numbers(n):
    if type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Error: Can't convert to integer")
    for i in range(n):
        print(i)


def calculate(operator, operand1, operand2):
    if type(operand1) != int or type(operand2) != int:
        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
        except ValueError:
            result = "Error: Can't convert to integer"
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    else:
        result = "Error: Invalid operator"
    return result


# ----------------


num1 = 10
num2 = 0
result = divide_numbers(num1, num2)
print(result)

my_list = [1, 2, 3]
index = 5
element = get_element_by_index(my_list, index)
print(element)


string1 = "Hello"
string2 = 123
result = concatenate_strings(string1, string2)
print(result)

num = "5"
print_numbers(num)

operator = "+"
operand1 = 5
operand2 = "2"
result = calculate(operator, operand1, operand2)
print("Result:", result)
