from pprint import pprint
#- Create a variable to hold the values of Nestle products (use a dicitionary)
kate_dict = {"KitKat" : 34456432 ,"Nescafe" : 14106132,"Maggi" : 9960312, "Nido" : 44506003}

#- Create a variable to hold the values of Unilever products (Use a dictionary)
dalia_dict= {"Lipton" : 23456000,"Breyers" : 1235891,"HellManns" : 17241412,"Marmite" : 11715324}

#- Print each product sold by Unilever and the sales figures / numbers  for that product.
for key, value in dalia_dict.items():
    print(key , str(value)+ " US Dollars")
print("\n")

#- Print each product sold by Nestle and the sales figures / numbers  for that product.
for key, value in kate_dict.items():
    print(key, str(value)+ " US Dollars")
print("\n")

#- Print which of the companies has more products that the other company.
if len(kate_dict) == len(dalia_dict):
    print("Nestle and Unilever have the same number of products")
elif len(kate_dict) > len(dalia_dict):
    print("Nestle have more products than Unilever")
else:
    print("Unilever have more products than Nestle")
print("\n")

#- Print the top selling product from Nestle with sales figures.
max_nestle = max(kate_dict, key = lambda x: kate_dict[x])
print("The top selling product from Nestle is {} with sales figures {} US Dollars ".format(max_nestle,kate_dict.get(max_nestle)))
print("\n")

#- Print the top selling product from Unilever with sales figures.
max_unilever = max(dalia_dict, key = lambda x: dalia_dict[x])
print("The top selling product from Unilever is {} with sales figures {} US Dollars ".format(max_unilever,dalia_dict.get(max_unilever)))
print("\n")

Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

def loop(massge,set_op):
    print(massge)
    for i in set_op:
        pprint(i)
    print("\n")

#- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
union = (Unilever | Nestle)
loop("Nestle and Unilever sells there products in this cities: ",union)

#- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Intersection = (Unilever & Nestle)
loop("the common cities betwean Nestle and Unilever: ",Intersection)

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
difference = (Nestle - Unilever)
loop("only Nestle sells in this cities: ",difference)