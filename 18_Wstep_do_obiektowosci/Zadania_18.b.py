# Stworzyć klasę `FoodItem` z polami `id`, `price` `item` - specjalnymi metodami `__init__` i `__repr__`, stworzyć listę `FoodItem` na podstawie pliku CSV

import os
import sys

print(os.getcwd())


class FoodItem:
    def __init__(self, id, price, item):
        self.id = id
        self.price = price
        self.item = item

    def __repr__(self):
        return f'FootItem("{self.id}", "{self.price}", "{self.item}")'


list = []

with open('..\\15_Pliki_tekstowe\\data\\foods.csv', 'r') as f:
    while line := f.readline():
        x = line.strip().split(",")
        list.append(FoodItem(x[0], x[1], x[2]))
        # print(x)
        #  print(f'{n:03d} {tab.join(line)}')

print(list)
