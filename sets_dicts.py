#1 - Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_products = {
    'KitKat':34.456 , 'Nescafe':14.106,
    'Maggi':9.960,'Nido':44.506}
 
 #2 - Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products = {
    'Lipton':23.456, 'Breyers':1.235,
    'HellManns':17.241,'Marmite':11.715}

#3 - Print each product sold by Nestle and the sales figures / numbers  for that product.
for key, value in nestle_products.items():
    print(key, ' : ', value)
print()

#4- Print each product sold by Unilever and the sales figures / numbers  for that product.
for key, value in unilever_products.items():
    print(key, ' : ', value)
print()
countries = {
    'Nestle' : ['Saudi Arabia', 'Oman', 'Kuwait', 'Egypt', 'Jordan', 'Sudan'],
    'Unilever' : ['Saudi Arabia', 'Kuwait', 'Iraq', 'Morocco', 'Yemen', 'United Emirates']
    }

# 5- Print which of the companies has more products that the other company.
if len(nestle_products.keys()) > len(unilever_products.keys()):
    print('nestle has more products')
elif nestle_products.keys() < unilever_products.keys():
    print('unilever has more products')
else:
    print('they have the same number of products')

# 6- Print the top selling product from Nestle with sales figures.
top_sale_nestla = max(nestle_products, key=nestle_products.get)
print('top selling product from Nestle is ', top_sale_nestla)

# 7- Print the top selling product from Unilever with sales figures.
top_sale_unilever = max(unilever_products, key=unilever_products.get)
print('top selling product from Unilever is ', top_sale_unilever)

#8 - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print('\nprint all the cities Unilever & Nestle sell their products in:')
print(set(countries['Nestle']).union(set(countries['Unilever'])))
print()

#9- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print('print the cities that both Nestle & Unilver sell in common: ')
print(set(countries['Nestle']).intersection(set(countries['Unilever'])))
print()

#10- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print('print the cities Nestle sells in , but Unilver does not sell in')
print(set(countries['Nestle']).difference(set(countries['Unilever'])))