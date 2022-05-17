#created dictionary for the products the company
nestle_products= {
    "KitKat": '34,456,432 $',
    "Nescafe": '14,106,132 $',
    "Maggi": '9,960,312 $',
    "Nido": '44,506,003 $'
}

unilever_products= {
    "Lipton": '23,456,000 $',
    "Breyers": '1,235,891 $',
    "HellManns": '17,241,412 $',
    "Marmite": '11,715,324 $'
}

print(unilever_products, "\n")

print(nestle_products, "\n")

#Comparison between companies products
print("-" * 80)
if len(nestle_products) > len(unilever_products):
   print("products Nestle is more products from Unilever " , nestle_products)

elif len(unilever_products)> len(nestle_products):
   print("Unilever is more products from Nestle " , unilever_products)

elif len(unilever_products) == len(nestle_products):
  print("products Nestle and Unilever is equal " , nestle_products, "\n" , unilever_products)

#the top selling product from Nestle with sales figures
print("-" * 80)
max_value= max(nestle_products), max(nestle_products.values())
print(max_value, "\n")

#the top selling product from Unilever with sales figures
max_value= max(unilever_products), max(unilever_products.values())
print(max_value, "\n")

print("-" * 80)
nestle_sell_in = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

unilever_sell_in = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
for element in nestle_sell_in:
    print(element)

print("-" * 80)
for element in unilever_sell_in:
    print(element)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common  
print("-" * 80)
for element in nestle_sell_in & unilever_sell_in:
    print(element)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("-" * 80)
for element in nestle_sell_in - unilever_sell_in:
    print(element)


