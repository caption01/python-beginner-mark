things = ('Car', 'Fan', 'Cup', 'Mug', 'Glass', 'Mug')
print(things)

# Number of times mug appear
mug_count = things.count('Mug')
print(f'Count of Mug: {mug_count}')

# Index of Mug
mug_idx = things.index('Mug')
print(f'Mug index: {mug_idx}')

# First item
first_item = things[0]
print(f'First item: {first_item}')

things[0] = 'New thing'