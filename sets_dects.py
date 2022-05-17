Nestle = {"KitKat" : 34456432, "Nescafe" : 14106132, "Maggi" : 9960312, "Nido" : 44506003}
Unilever = {"Lipton" : 23456000,"Breyers": 1235891 ,"HellManns" : 17241412 , "Marmite" : 11715324}
key_list_Unilever = list(Unilever.keys())
value_list_Unilever = list(Unilever.values())
key_list_Nestle = list(Nestle.keys())
value_list_Nestle = list(Nestle.values())
length_Unilever = len(Unilever)
length_Nestle = len(Nestle)

print("The Unilever products")
for item in range(1,length_Unilever):
    print('the product' ,key_list_Unilever[item],'sales numbers for this product', value_list_Unilever[item] , 'US Dollars' )

print("The Nestle products")
for item in range(1,length_Nestle):
    print('the product' ,key_list_Nestle[item],'sales numbers for this product', value_list_Nestle[item] , 'US Dollars' )

print("Which company has the biggest sales?")
if key_list_Nestle == key_list_Nestle :
    print("Sales are equal")
elif key_list_Nestle > key_list_Unilever :
    print("The sales of Nestle are higher than Unilever")
else:
    print("The sales of Nestle are less than Unilever")


TopsellingproductNestle = 0
for n in value_list_Nestle :
    if n >TopsellingproductNestle:
        TopsellingproductNestle= n
TheProduct=value_list_Nestle.index(TopsellingproductNestle)
print('the top selling product is' ,key_list_Nestle[TheProduct],'sales figures',TopsellingproductNestle)

TopsellingproductUnilever = 0
for n in value_list_Unilever :
    if n >TopsellingproductUnilever:
        TopsellingproductUnilever= n
TheProduct=value_list_Unilever.index(TopsellingproductUnilever)
print('the top selling product is' ,key_list_Unilever[TheProduct],'sales figures',TopsellingproductUnilever)

SetOfCityOfUnilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
SetOfCityOfNestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
print("Unilever Cities :")
for item in SetOfCityOfUnilever :
    print(item)

print("Nestle Cities :")
for item in SetOfCityOfNestle :
    print(item)

print("Common cities between Nestle and Unilever :")
common_cities_set = SetOfCityOfUnilever.intersection(SetOfCityOfNestle)
for item in common_cities_set :
    print(item)

print("Cities Nestle sells in")
all_visited_cities_set = SetOfCityOfNestle.difference(SetOfCityOfUnilever)
print(all_visited_cities_set)