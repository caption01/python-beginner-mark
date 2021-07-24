fruit = ['Apple', 'Orange', 'Pear', 'Apple', 'Lemon']

print(fruit)

# Convert to set
fruit_set = set(fruit)
print(f'Fruit Set: {fruit_set}')

uniqe_fruit_list = list(fruit_set)
print(f'Uniqe fruit list {uniqe_fruit_list}')

# Makr list unique (short)
uniqe_list = list(set(fruit))
print(f'Uniqe fruit list: {uniqe_list}')