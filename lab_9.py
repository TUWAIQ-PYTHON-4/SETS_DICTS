#Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products = {'KitKat' : 34456432, 'Nescafe': 14106132, 'Maggi' : 9960312, 'Nido' : 44506003}

#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products  = {'Lipton' : 23456000,'Breyers' : 1235891 ,'HellManns' : 17241412 ,'Marmite': 11715324}

#Print each product sold by Unilever and the sales figures / numbers for that product.
for products , sales in Unilever_products.items():
    print(products +" _ "+ str(sales))

#Print each product sold by Nestle and the sales figures / numbers for that product.
for products , sales in Nestle_products.items():
    print(products +" _ "+ str(sales))

#Print which of the companies has more products that the other company.
if len(Unilever_products.keys()) > len(Nestle_products.keys()):
    print("Unilever has the more products than Nestle")
elif len(Unilever_products.keys())  < len(Nestle_products.keys()):
    print("Nestle has the more products than Unilever")
else:
    print("There are equal")

#Print the top selling product from Nestle with sales figures.
top_selling_Nestle = max(Nestle_products.values())
print(top_selling_Nestle)

#Print the top selling product from Unilever with sales figures.
top_selling_Unilever = max(Unilever_products.values())
print(top_selling_Unilever)

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(Nestle | Unilever)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(Nestle & Unilever)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(Nestle - Unilever)


"""for products , sales in Nestle_products.items():
    top_selling_Nestle = max(str(sales))
    print(top_selling_Nestle)    """

    


"""Nestle_products = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}"""

"""Unilever_products = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}"""



print(type(Nestle_products))