global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 1:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1  # Decrement local_variable

    return numbers

my_set = {1, 2, 3, 4, 5}

result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable  # Add a new key-value pair

# Call modify_dict to modify my_dict
modify_dict()

def update_global():
    global global_variable
    global_variable += 10  # Increment global_variable by 10

    for i in range(5):
        print(i)

# Call update_global
update_global()

if my_set is not None and my_dict.get('key4') == 10:  # Check if my_dict['key4'] exists and is equal to 10
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)