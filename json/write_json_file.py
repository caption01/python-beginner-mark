import os
import json

current_dir = os.getcwd()
dir_path = os.path.join(current_dir, 'output')
os.makedirs(dir_path, exist_ok=True)
json_path = os.path.join(dir_path, 'user.json')

user = {
    'name': 'Mike',
    'age': 23,
    'is_active': True,
    'fav_nums': [1,6,3,8,3]
}

with open(json_path, 'w') as jf:
    json.dump(user, jf, sort_keys=True, indent=2)


