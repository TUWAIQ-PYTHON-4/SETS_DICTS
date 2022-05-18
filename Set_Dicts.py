from pprint import pprint
from re import I


Nestle_ = { 'KitKat' :34456432, 
           'Nescafe':14106132 , 
           'Maggi'  :9960312, 
           'Nido'   :44506003}

Unilever_={'Lipton':23456000, 
        'Breyers':1235891, 
        'HallManns':17241412, 
        'Marmite':11715324}
pprint(Nestle_)

pprint(Unilever_)        
Nestle = {"Saudi Arabia", "Oman", "Kuwait","Egypt","Jordan","Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq","Morocco","Yemen","United Emirates"}



if len(Nestle_.keys()) > len(Unilever_.keys()):
    pprint("Nestle has more products than Unilever")
else:
    pprint("Unilever has more products than Nestle")
'''
for x in Nestle:
  print(x)



for x in Unilever:
  print(x)  
'''
print(Nestle|Unilever)
print(Nestle&Unilever)
print(Nestle-Unilever) 


T_Seller = [(value, key) for key,
 value in Nestle_.items()]
print(max(T_Seller))

T_Seller = [(value,key) for key,
 value in Unilever_.items()]
print(max(T_Seller))

