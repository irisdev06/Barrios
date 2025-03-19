import csv
import json

with open("csv-json/customers.csv", mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    rows = list(csv_reader)

with open("customersjs.json", mode='w', encoding='utf-8') as jsonf:
    json.dump(rows, jsonf, indent=4, ensure_ascii=False)

