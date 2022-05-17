#Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products={"KitKat":34456432 ,"Nescafe":14106132,"Maggi":9960312 ,"Nido":44506003}

#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products={"Lipton": 2345600 ,"Breyers":1235891,"HellManns":17241412,"Marmit":11715324}

#Print each product sold by Unilever and the sales figures / numbers for that product.
print("\nThe information for unilever products :")
for key1, value1 in Unilever_products.items():
    print(key1, ' : ', value1)

#Print each product sold by Nestle and the sales figures / numbers for that product.
print("\nThe information for nestle products :")
for key2, value2 in Nestle_products.items():
    print(key2, ' : ', value2)
print("\n____________________________________________\n")
#Print which of the companies has more products that the other company.
value_Nestle = len(Nestle_products)
value_Unilever = len(Unilever_products)
print("Compare number of products:")
if value_Nestle > value_Unilever:
    print("The company have more prodects is Nestle")
elif value_Nestle < value_Unilever:
    print("The company have more prodects is Unilever")
else:
     print("\n All companies have the same number of products")
print("\n____________________________________________\n")
#Print the top selling product from Nestle with sales figures.
max_value = max(Nestle_products.values())  
max_keys = [k for k, v in Nestle_products.items() if v == max_value] 
print(" Top selling product in nestle :",max_value, max_keys)

#Print the top selling product from Unilever with sales figures.
max_value = max(Unilever_products.values())  
max_keys = [k for k, v in Unilever_products.items() if v == max_value] 
print(" Top selling product in unilever : ",max_value, max_keys)

Nestle_set ={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_set = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("\n____________________________________________\n")
# print all the cities Unilever & Nestle sell their products in.

print("\n All the cities Unilever & Nestle sell their products in :\n")
list1=[]
for i in Nestle_set | Unilever_set:
    list1.append(i)
print(list1)
#print the cities that both Nestle & Unilver sell in common.
print("\n The cities that both Nestle & Unilver sell in common : \n")
list2=[]
for i in Nestle_set & Unilever_set:
    list2.append(i)
print(list2)
#print the cities Nestle sells in , but Unilver doens't sell in.
print("\n The cities Nestle sells in , but Unilver doens't sell in: \n")
list3=[]
for i in Nestle_set - Unilever_set:
    list3.append(i)
print(list3)
