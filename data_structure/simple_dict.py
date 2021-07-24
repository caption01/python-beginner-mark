dog = {
    'name': 'Daisy',
    'breed': 'Chihuahua',
    'color': 'Fawn',
}
print(dog)

dog['age'] = 10
print(dog)

dog['age'] = 11
print(dog)

age = dog.pop('age')
print(f'Remove age: {age}')
print(dog)

age = dog.get('age', 'Age not set')
print(f'Age after removing it: {age}')

dog.clear()
print(dog)