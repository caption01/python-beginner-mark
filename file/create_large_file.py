import os

with open('numbers.txt', 'w') as num_files:
    for num in range(1, 1000001):
        num_files.write(f'{num}\n')
    
print('Finishes creating large file')