import os
import csv

total_stock = 0

with open('output/store.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for product in reader:
        quantity_in_product = int(product['Quantity'])
        total_stock += quantity_in_product

print(f'Total stock: {total_stock}')

