import csv

with open('price.csv', encoding='utf8') as csv_file:
    price = csv.DictReader(csv_file)
    for item in price:
        print(item)

with open('price_write.csv', mode='w', encoding='utf8')as csv_file:
    fieldnames = ['S/N','ITEM','QTY','RATE','AMOUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
