names = ['Brooke', 'Mark', 'Daisy']

# Update name by index
names[2] = 'Diva'

# Append name
names.append('Bombay')

# Extends list with 3 more item
names.extend(['Sushi', 'Susa', 'Siya'])

# Remove name
names.remove('Bombay')

# Remove first name form list
removed_from_list = names.pop(0)
print(f'Removed: {removed_from_list}')

# Print list of names
print(names)

# Print name as specific index
print(names[0])


if 'Sushi' in names:
    print('Sushi in the list')

if 'Bombay' not in names:
    print('Bombay not in a list')