dic_Nestle ={'kitkat':'34,456,432 ','Nescafe':'14,106,132 ','Maggi':'9,960,312 ','Nido':'44,506,003'}
for key, value in dic_Nestle.items():
    print(key,':',value)

dic_Unilever ={'Lipton':'23,456,000','Breyers':'1,235,891','HellManns':'17,241,412','Marmite':'11,715,324'}
for key, value in dic_Unilever.items():
    print(key,':',value)

new_comp= dic_Nestle,dic_Unilever
max_length = max(map(len, new_comp))
print("Nestle and Unilever has the same number of product",[x for x in new_comp if len(x) == max_length])


max_sale1 = max(dic_Nestle,key=dic_Nestle.get)
print("The TOP selling product in Nestle is :",max_sale1)

max_sale2 = max(dic_Unilever,key=dic_Unilever.get)
print("The TOP selling product in Unilever is :",max_sale2)

citis_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"} 
citis_Unilever ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(citis_Nestle | citis_Unilever) 
print(citis_Nestle & citis_Unilever)
print(citis_Nestle - citis_Unilever)
