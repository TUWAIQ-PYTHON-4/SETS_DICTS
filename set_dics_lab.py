dic_Nestle ={'kitkat':'34,456,432 ','Nescafe':'14,106,132 ','Maggi':'9,960,312 ','Nido':'44,506,003'}
print("Nestle :")
for key, value in dic_Nestle.items():
    print(key,':',value)

dic_Unilever ={'Lipton':'23,456,000','Breyers':'1,235,891','HellManns':'17,241,412','Marmite':'11,715,324'}
print("Unilever :")
for key, value in dic_Unilever.items():
    print(key,':',value)


nestle_pro = len(dic_Nestle)
unilever_pro =len(dic_Unilever)
if nestle_pro > unilever_pro:
    print("Nestle has more product")
elif unilever_pro > nestle_pro:
    print("Unilever has more product")
else:
    print("Nestle and Unilever has the same number of product")

nestle_max = max(dic_Nestle.values())
max_key =[k for k,v in dic_Nestle.items() if v== nestle_max]
print("The TOP selling product in Nestle is" ,max_key, nestle_max,"Us dollar")

unilever_max = max(dic_Unilever.values())
max_key2 =[k for k,v in dic_Unilever.items() if v== unilever_max]
print("The TOP selling product in Unilever is" ,max_key2, unilever_max,"Us dollar")


citis_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"} 
citis_Unilever ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for n in citis_Nestle.union(citis_Unilever):
    print(n , end=' - ')
print("\n")
for c in citis_Nestle.intersection(citis_Unilever):
    print(c, end=' - ')
print("\n")
for a in citis_Nestle.difference(citis_Unilever):
    print(a, end=' - ')
