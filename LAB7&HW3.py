# Create a variable to hold the values of Nestle products (use a dicitionary)
from math import prod
from optparse import Values


nestle_products_dict = {"KitKat" : 34456432 , "Nescafe" : 14106132 , "Maggi" : 9960312 , "Nido" : 44506003 }

# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products_dict = {"Lipton" : 23456000, "Breyers" : 1235891 , "HellManns" : 17241412 , "Marmite" : 11715324 }

# Print each product sold by Unilever and the sales figures / numbers for that product.
for product, sales in unilever_products_dict.items():
    print(product, sales, "USD")

# Print each product sold by Nestle and the sales figures / numbers for that product.
print("") # new line
for product, sales in nestle_products_dict.items():
    print(product, sales, "USD")

# Print which of the companies has more products that the other company.
print("") # new line
if len(unilever_products_dict.keys()) > len(nestle_products_dict.keys()):
    print ("Unilever has more products")
if len(nestle_products_dict.keys()) > len(unilever_products_dict.keys()):
    print("Nestle has more products")
else:
    print("They both have the same number of products")

# Print the top selling product from Nestle with sales figures.
print("") # new line
print ("The top selling prodcuts from Nestle is:", max(nestle_products_dict, key=nestle_products_dict.get) , (max(nestle_products_dict.values())), "USD")

# Print the top selling product from Unilever with sales figures.
print("") # new line
print ("The top selling prodcuts from Unilever is:", max(unilever_products_dict, key=unilever_products_dict.get) , (max(unilever_products_dict.values())), "USD")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("") # new line
nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"} 
unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
for cit in nestle_set.union(unilever_set):
    print(cit, end=" | ")

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("") # new line
for cit in nestle_set.intersection(unilever_set):
    print(cit, end=" | ")

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("") # new line
for cit in nestle_set.difference(unilever_set):
    print(cit, end=" | ")
 
'''
OUTPUT:

Lipton 23456000 USD
Breyers 1235891 USD
HellManns 17241412 USD
Marmite 11715324 USD

KitKat 34456432 USD
Nescafe 14106132 USD
Maggi 9960312 USD
Nido 44506003 USD

They both have the same number of products

The top selling prodcuts from Nestle is: Nido 44506003 USD

The top selling prodcuts from Unilever is: Lipton 23456000 USD

Egypt | Saudi Arabia | Sudan | United Emirates | Iraq | Kuwait | Morocco | Oman | Yemen | Jordan |
Kuwait | Saudi Arabia |
Egypt | Oman | Sudan | Jordan |

'''