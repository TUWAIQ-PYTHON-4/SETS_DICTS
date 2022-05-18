
Nestle_prodects_sales = {
    'KitKat' : '34456432' ,
    'Nescafe' : '14106132',
    'Maggi' : '9960312' ,
    'Nido' : '44506003' ,
}
Unilever_products_sales = {
 'Lipton' : '23456000' ,
 'Breyers' : '1235891' ,
 'HellManns' : '17241412',
 'Marmite' : '11715324' ,
}

#  Print each product sold by Nestle and the sales figures / numbers  for that product.
print(Nestle_prodects_sales.items())
print(Unilever_products_sales.items())

# Print which of the companies has more products that the other company.
N_list_of_keys = list(Nestle_prodects_sales.keys())
len_Nestle_pro = len(N_list_of_keys)

U_list_of_keys = list(Unilever_products_sales.keys())
len_Unilever_pro = len(U_list_of_keys)

if len_Unilever_pro == len_Nestle_pro:
    print('\nBoth Nestle and Unilever has the same amount of prodects')
elif len_Unilever_pro < len_Nestle_pro:
    print(f'\nUnilever has {len_Unilever_pro} prodects, which is more than Nestle')
else:
    print(f'\nNestle has {len_Nestle_pro} prodects, which is more than Unilever ')



'''
Print the top selling product from Nestle with sales figures.
Print the top selling product from Unilever with sales figures.
'''
N_list_of_val = [int(i) for i in Nestle_prodects_sales.values()]
U_list_of_val = [int(i) for i in Unilever_products_sales.values()]

N_top_seling = max(N_list_of_val)
U_top_seling = max(U_list_of_val)

x1 =  N_list_of_val.index(N_top_seling)
print(f'\nThe top selling product from Nestle is {N_list_of_keys[x1]}: {N_top_seling} USD')

x2 = U_list_of_val.index(U_top_seling)
print(f'The top selling product from Unilever is {U_list_of_keys[x2]}: {U_top_seling} USD')

'''
Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
'''

Nestle = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


print('\nNestle sel in:')
for i in Nestle:
  print(i)

print('\nUnilever sel in:')
for j in Unilever:
    print(j)


'''
Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
'''
intersect = Nestle.intersection(Unilever)
print('\nNestle & Unilever: ')
for i in intersect:
    print(i)


'''
Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''
difference = Nestle.difference(Unilever)
print('\nNestle ^ Unilever: ')
for i in difference:
    print(i)
