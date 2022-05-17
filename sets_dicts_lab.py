# Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_products = {"KitKat":"34,456,432", "Nescafe" : "14,106,132", "Maggi" : "9,960,312", "Nido" : "44,506,003"}

# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products = {"Lipton":"23,456,000", "Breyers" : "1,235,891", "HellManns" : "17,241,412", "Marmite" : "11,715,324"}

# Print each product sold by Unilever and the sales figures / numbers for that product.
for product in unilever_products:
    print(product,unilever_products[product])

# Print each product sold by Nestle and the sales figures / numbers for that product.
for product in nestle_products:
    print(product,nestle_products[product] )

# Print which of the companies has more products that the other company.
nestle_products_sales=0
unilever_products_sales=0
for product in nestle_products:
    nestle_products_sales+=int(nestle_products[product].replace(',',''))
for product in unilever_products:
    unilever_products_sales+=int(unilever_products[product].replace(',',''))
if nestle_products_sales == unilever_products_sales:
    print("Both companies have equal products sales")
elif nestle_products_sales < unilever_products_sales:
    print("Unilever has more products sales")
else:
    print("Nestle has more products sales")

# Print the top selling product from Nestle with sales figures. !!
values_list=[]
key_list=[]
for key, value in nestle_products.items():
    value_int= int(value.replace(',',''))
    values_list.append(value_int)
    key_list.append(key)

max_value= max(values_list)
index_of_max=values_list.index(max(values_list))
print(f"The top selling product from Nestle is {key_list[index_of_max]} with sales {max_value}.")

# Print the top selling product from Unilever with sales figures. !!
values_list2=[]
key_list2=[]
for key, value in unilever_products.items():
    value_int= int(value.replace(',',''))
    values_list2.append(value_int)
    key_list2.append(key)

max_value2= max(values_list2)
index_of_max2=values_list2.index(max(values_list2))
print(f"The top selling product from Unilever is {key_list2[index_of_max2]} with sales {max_value2}.")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
nestle_set= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_set= {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

all_cities_set= nestle_set.union(unilever_set)
print("All the cities Unilever & Nestle sell their products in: ")
for member in all_cities_set:
     print(member)

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
common_cities_set= nestle_set.intersection(unilever_set)
print("The cities that both Nestle & Unilver sell in common: ")
for member in common_cities_set:
     print(member)

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
diff_cities_set= nestle_set.difference(unilever_set)
print("The cities Nestle sells in, but Unilver doens't sell in: ")
for member in diff_cities_set:
     print(member)