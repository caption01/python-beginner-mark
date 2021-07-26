cart = []

try:
    item = cart[1]
except IndexError as e:
    print(f'Index not found')