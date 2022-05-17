nestle_products ={"KitKat" : "34,456,432 US Dollars", "Nescafe" : "14,106,132 US Dollars","Maggi" : "9,960,312 US Dollars",
"Nido" : "44,506,003 US Dollars"}


unilever_products ={"Lipton" : "23,456,000 US Dollars", "Breyers" : "1,235,891 US Dollars",
"HellManns" : "17,241,412 US Dollars", "Marmite" : "11,715,324 US Dollars"}
#Print each product sold by Unilever and the sales figures / numbers for that product.
print(nestle_products)
print("product sold by Unilever:")
for i in nestle_products:
    print(i,nestle_products[i])
#Print each product sold by Nestle and the sales figures / numbers for that product
print("product sold by Nestle:")
for s in unilever_products:
    print(s,unilever_products[s])
#Print which of the companies has more products that the other company.
print("companies has more products:")
size_nestle =format(len(nestle_products))
size_unilever =format(len(unilever_products))
if size_nestle>size_unilever:
    print("nestle_products")
elif size_nestle<size_unilever:
    print("size_unilever")
else:
    print("same products*** ")
#Print the top selling product from Nestle with sales figures.
print(max(nestle_products)," ",nestle_products[i])
#Print the top selling product from Unilever with sales figures.
print("Print the top selling product from Unilever with sales figures:")
print(max(unilever_products)," ",unilever_products[s])

countries_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
countries_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("Using Sets & a loop, print all the cities Unilever & Nestle sell their products in:")
union = countries_nestle.union(countries_unilever)
for u in union:
    print(u)
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("print the cities that both Nestle & Unilver sell in common:")
intersection = countries_nestle.intersection(countries_unilever)
for ii in intersection:
    print(ii)

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

print("print the cities Nestle sells in , but Unilver doens't sell in.")
difference = countries_nestle.difference(countries_unilever)
for dd in difference:
    print(dd)








