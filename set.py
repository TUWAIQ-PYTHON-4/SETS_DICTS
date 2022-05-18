Nestle_pro ={"kitkat":34456432  ,"nescafe":14106132,"maggi":9960312 ,"nido":44506003 }
Unilever_pro={"lipton":23456000,"breyers":1235891,"hellmanns":17241412,"marmite":11715324}

country_of_nestla = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
country_of_unil ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print(Nestle_pro)
print(Unilever_pro)

if len (Nestle_pro.keys()) >len (Unilever_pro.keys()):
    print("NEstle product more than Unilver")
elif len (Nestle_pro.keys()) >len (Unilever_pro.keys()):
         print("NEstle product more than Unilver")
else :
              print("the product of Nestle and Unilver equal")

print(Nestle_pro.keys())
print(Unilever_pro.keys())





max_nestle = max(Nestle_pro, key=Nestle_pro.get  )
max_unil = max(Unilever_pro, key=Unilever_pro.get)
print("Maximum value on nestle:",max_nestle)
print("Maximum value on Unilever:",max_unil)

city_of_ns_un=country_of_nestla .union(country_of_unil)
print(city_of_ns_un)

print(country_of_nestla & country_of_unil )
print(country_of_nestla - country_of_unil )

