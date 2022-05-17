
Kate_Nestle = {"KitKat":"34,456,432 US Dollars","Nescafe":"14,106,132 US Dollars","Maggi":" 9,960,312 US Dollars","Nido":"44,506,003 US Dollars"}


Dalia_Unilever= {"Lipton":"23,456,000 US Dollars","Breyers":"1,235,891 US Dollars","HellManns":"17,241,412 US Dollars","Marmite":"11,715,324 US Dollars"}

Monica_Nestle={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Monica_Unilever={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("sold by Unilever",Dalia_Unilever)
print("sold by Nestle",Kate_Nestle)



top_seller = [(value, key) for key, value in Kate_Nestle.items()]
print(max(top_seller))

top_seller = [(value,key) for key, value in Dalia_Unilever.items()]
print(max(top_seller))


print(Monica_Nestle|Monica_Unilever)
print(Monica_Nestle&Monica_Unilever)
print(Monica_Nestle-Monica_Unilever)