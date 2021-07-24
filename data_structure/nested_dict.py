dog = {
    'name': 'Otis',
    'breed': 'Pug',
    'owner': {
        'name': 'Mark',
        'age': 31
    },
    'favorite': ['meat', 'ball']
}

print(dog)

owner_name = dog['owner']['name']
print(owner_name)