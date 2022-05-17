

# - Create a variable to hold the values of Nestle products (use a dicitionary)

nestle_products = {'KitKat' : 34456432 , 'Nescafe' : 14106132,
                    'Maggi' : 9960312 , 'Nido' : 44506003}

#- Create a variable to hold the values of Unilever products (Use a dictionary)

unilever_products = {'Lipton' : 23456000, 'Breyers' : 1235891,
                     'HellManns' : 17241412, 'Marmite' : 11715324}

# - Print each product sold by Unilever and the sales figures / numbers  for that product.
#- Print each product sold by Nestle and the sales figures / numbers  for that product.

print(nestle_products)
print(unilever_products)

#- Print which of the companies has more products than the other company.

if len(nestle_products) > len(unilever_products):
    print("Nestle has more products than Unilever")

elif len(nestle_products) < len(unilever_products):
    print("Unilever has more products than Nestle")

else:
   print("Nestle and Unilever have the same amount of products") 


print('Top selling:\n')

# Print the top selling product from Nestle with sales figures.

n_top_selling=0

for proudct, sales in nestle_products.items():
    if sales > n_top_selling:
        n_top_selling= sales

for proudct, sales in nestle_products.items():
    if n_top_selling == sales:
        print(f"top selling product of nestle is {proudct}\n")

# Print the top selling product from Unilever with sales figures.

u_top_selling=0

for proudct, sales in unilever_products.items():
    if sales > u_top_selling:
        u_top_selling= sales

for proudct, sales in unilever_products.items():
    if u_top_selling == sales:
        print(f"top selling product of nestle is {proudct}\n")




nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"} 



# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("Unilever and Nestle sell their products in the following cities:" )
for city in (nestle_countries | unilever_countries):
    print(city)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

print("Cities that sells both Unilever and Nestle:")

for city in (nestle_countries & unilever_countries):
    print(city)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("Cities that sells only Nestle:")

for city in (nestle_countries - unilever_countries):
    print(city)