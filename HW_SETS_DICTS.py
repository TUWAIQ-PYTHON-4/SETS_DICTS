

# Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_products={"KitKat":"34,456,432 US Dollars" , "Nescafe" : "14,106,132 US Dollars" , "Maggi" : "9,960,312 US Dollars" , "Nido" : "44,506,003 US Dollars"}
# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products={"Lipton":"23,456,000 US Dollars","Breyers":"1,235,891 US Dollars", "HellManns" : "17,241,412 US Dollars", "Marmite" :"11,715,324 US Dollars"}

# Print each product sold by Unilever and the sales figures / numbers  for that product.
print("unilever_products:")
for key , Value in unilever_products.items():
    print(key,Value)
# Print each product sold by Nestle and the sales figures / numbers  for that product.
print("nestle products:")
for key , Value in nestle_products.items():
    print(key,Value)
# Print which of the companies has more products that the other company
prod_nestle=len(nestle_products)
prod_unilever=len(unilever_products)
if prod_nestle > prod_unilever:
    print("nestle")
elif prod_unilever>prod_nestle:
    print("unilever")
else:
    print("the number of prodect same")

# Print the top selling product from Nestle with sales figures.
max_selling_nestle=max(nestle_products.values())
max_prod_nestle=[key for key, list_of_values in nestle_products.items() if max_selling_nestle == list_of_values]
print("Top selling product from unilever:",max_prod_nestle,max_selling_nestle)

# Print the top selling product from Unilever with sales figures.
max_selling_unilever=max(unilever_products.values())
max_prod_unilever=[key1 for key1, list_of_values in unilever_products.items() if max_selling_unilever == list_of_values]
print("Top selling product from unilever:",max_prod_unilever,max_selling_unilever)

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
nestle={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("Display all the cities Unilever & Nestle sell their products in:")
val = [print(item) for item in nestle | unilever]

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("Display the cities that both Nestle & Unilver sell in common:")
val = [print(item) for item in nestle & unilever]

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in
print("Display cities Nestle sells in , but Unilver doens't sell in:")
val = [print(item) for item in nestle.difference(unilever)]

