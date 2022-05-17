Nestle_roducts={"KitKat" : "34,456,432 US Dollars","Nescafe" : "14,106,132 US Dollars","Maggi" : "9,960,312 US Dollars","Nido" : "44,506,003 US Dollars"}
Unilever_products={"Lipton" : "23,456,000 US Dollars","Breyers" : "1,235,891 US Dollars","HellManns" : "17,241,412 US Dollars","Marmite" : "11,715,324 US Dollars"}

for key ,value in Unilever_products.items():
    print(key,value)
for key ,value in Nestle_roducts.items():
    print(key,value)

print("Nestle products are {}".format(len(Nestle_roducts)),"Unilever products are {}".format(len(Unilever_products)))







Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for items in Nestle:
    print(items)

for element in (Nestle & Unilever):
    print(Nestle & Unilever)

for element in (Nestle & Unilever):
    print(Nestle - Unilever)