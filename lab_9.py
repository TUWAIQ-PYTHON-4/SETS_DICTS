#Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products = {'KitKat' : 34456432, 'Nescafe': 14106132, 'Maggi' : 9960312, 'Nido' : 44506003}

#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products  = {'Lipton' : 23456000,'Breyers' : 1235891 ,'HellManns' : 17241412 ,'Marmite': 11715324}

#Print each product sold by Unilever and the sales figures / numbers for that product.
print("product sold by Unilever and the sales figures: ")
for products , sales in Unilever_products.items():
    print(products +" _ "+ str(sales))
print("\n")

#Print each product sold by Nestle and the sales figures / numbers for that product.
print("product sold by Nestle and the sales figures: ")
for products , sales in Nestle_products.items():
    print(products +" _ "+ str(sales))
print("\n")
#Print which of the companies has more products that the other company.
print("which of the companies has more products that the other company:")
if len(Unilever_products.keys()) > len(Nestle_products.keys()):
    print("Unilever has the more products than Nestle")
elif len(Unilever_products.keys())  < len(Nestle_products.keys()):
    print("Nestle has the more products than Unilever")
else:
    print("There are equal")
print("\n")

#Print the top selling product from Nestle with sales figures.
fin_max = max(Nestle_products, key=Nestle_products.get)
print("Maximum value in Nestle:",fin_max)
print("\n")

#Print the top selling product from Unilever with sales figures.
fin_max = max(Unilever_products, key=Unilever_products.get)
print("Maximum value in Unilever:",fin_max)
print("\n")

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("The cities Unilever & Nestle sell their products in:")
for i in Nestle | Unilever:
    print(i ,end=" , ")
print("\n")

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("The cities that both Nestle & Unilver sell in common:")
for i in Nestle & Unilever:
    print(i ,end=" , ")
print("\n")


#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("The cities Nestle sells in , but Unilver doens't sell in:")
for i in Nestle - Unilever:
    print(i ,end=" , ")
print("\n")
