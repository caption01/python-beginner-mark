import os
import json

curr_dir = os.getcwd()
dir_path = os.path.join(curr_dir, 'output')
json_path = os.path.join(dir_path, 'user.json')

with open(json_path) as jf:
    user = json.load(jf)

print(user)

fav_nums = user['fav_nums']
print(fav_nums)