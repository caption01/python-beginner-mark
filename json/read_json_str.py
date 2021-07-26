import json
import os

car_str = '{"make": "Tesla", "model": "Model Y"}'
car = json.loads(car_str)

print(car['model'])

nums_str = '[1,2,3]'
nums = json.loads(nums_str)

print(nums)