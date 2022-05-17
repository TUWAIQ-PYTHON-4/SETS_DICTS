Nestle = {"Nestle":23456000 ,"Nescafe":14106132 ,"Maggi":9960312 ,"Nido":44506003 }
Unilever = {"Lipton":34456432  ,"Breyers":1235891 ,"HellManns":17241412 ,"Marmite":11715324 }

listK1=list(Nestle.keys())
listV1= list(Nestle.values())
listK2=list(Unilever.keys())
listV2= list(Unilever.values())

for key, value in Nestle.items():
    print(key, value)
for key, value in Unilever.items():
    print(key, value)
if max(listV1)>max(listV2):
    print("Nestle")
else  :   
    print("Unilever")


position = listV1.index(max(listV1))
print(listK1[position],max(listV1))
position = listV2.index(max(listV2))
print(listK2[position],max(listV2))

NestleSet = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
UnileverSet = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("union") 
cities_set = NestleSet.union(UnileverSet)
for member in cities_set:
    print(member)
print("intersection")      
commonCitieSet = NestleSet.intersection(UnileverSet)
for member in commonCitieSet:
    print(member)
print("difference")    
differenceCitiesSet = NestleSet.difference(UnileverSet)
for member in differenceCitiesSet:
    print(member)