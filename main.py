Nestle_dicts = {
"KitKat" : "34,456,432 US Dollars" ,
"Nescafe" : "14,106,132 US Dollars" ,
"Maggi" :  "9,960,312 US Dollars ",
 "Nido": "44,506,003 US Dollars "
}


Unilever_dicts = {
"Lipton" : "23,456,000 US Dollars ", 
"Breyers" : "1,235,891 US Dollars " ,
"HellManns" : "17,241,412 US Dollars " ,
"Marmite" : "3,715,324 US Dollars " 
}

monica_nestla = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
monica_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for key, value in Unilever_dicts.items():
    print(key, value + "\n")
print("--------------------------------------")
for key, value in Nestle_dicts.items():
    print(key, value + "\n")
print("--------------------------------------")

if len(Nestle_dicts.keys()) > len(Unilever_dicts.keys()):
    print(" Nestle has more products ")

elif len(Unilever_dicts.keys()) > len(Nestle_dicts.keys()):
    print(" Unilever has more products ")

else :
    print(" Nestle and Unilever has same product ")
print("--------------------------------------")
values = []
keys = []

for key, value in Nestle_dicts.items():
    keys.append(key)
    values.append(int(value.split(" ")[0].replace(",","")))
print("The top selling in nestla ls :", keys[(values.index(max(values)))]," and the value is ", max(values),"$")

values = []
keys = []
print("--------------------------------------")
for key, value in Unilever_dicts.items():
    keys.append(key)
    values.append(int(value.split(" ")[0].replace(",","")))
print("The top selling in Unilever ls :", keys[(values.index(max(values)))]," and the value is ", max(values),"$")

print("--------------------------------------")
all_cities_Unilever_Nestle = monica_nestla.union(monica_Unilever)
print(all_cities_Unilever_Nestle)
print("--------------------------------------")
common_cities_Unilever_Nestle = monica_nestla.intersection(monica_Unilever)
print(common_cities_Unilever_Nestle)
print("--------------------------------------")
difference_cities_Unilever_Nestle= monica_nestla.difference(monica_Unilever)
print(difference_cities_Unilever_Nestle)



