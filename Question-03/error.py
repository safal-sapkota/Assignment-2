global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'valuy3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 1:  # Syntax issue here
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable = 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)  # Syntax issue: wrong function call

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict(5)  # Syntax issue: modify_dict does not take any arguments

def update_global():
    global global_variable
    global_variable += 10
    for i in range(5):
        print(i)
    I += 1  # Syntax issue: this is an undefined variable

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)