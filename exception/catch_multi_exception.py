from typing import final


cart = [
    {'name': 'Pencil'},
    {'name': 'Paper'},
    {'name': 'Stapler'}
]

try:
    item = cart[3]
    product = item['name']
except IndexError:
    print(f'not in cart')
except KeyError:
    print(f'product key not found')   
else:
    print(f'product: {product}') 
finally:
    print(f'finished checking')