from pprint import pprint


      

## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars
      

## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
#- Create a variable to hold the values of Nestle products (use a dicitionary)
nestle = {'KitKat':23456000,'Nescafe':14106132,'Maggi':9960312,'Nido':44506003}

#- Create a variable to hold the values of Unilever products (Use a dictionary)
unilever = {'Lipton':23456000,'Breyers':1235891,'HallManns':17241412,'Marmite':11715324}

#- Print each product sold by Unilever and the sales figures / numbers  for that product.
pprint(unilever)

#- Print each product sold by Nestle and the sales figures / numbers  for that product.
pprint(nestle)

#- Print which of the companies has more products that the other company.
if len(nestle.keys()) > len(unilever.keys()):
    pprint("Nestle has more products than Unilever")
else:
    pprint("Unilever has more products than Nestle")

#- Print the top selling product from Nestle with sales figures.
max_nestle = max(nestle, key = lambda x: nestle[x])
print("The top selling product from Nestle is {} with sales figures {} ".format(max_nestle,nestle.get(max_nestle)))

#- Print the top selling product from Unilever with sales figures.
max_unilever = max(unilever, key = lambda x: unilever[x])
print("The top selling product from Unilever is {} with sales figures {} ".format(max_unilever,unilever.get(max_unilever)))

#- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
countries_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
countries_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

nestle_unilever_union = (countries_nestle | countries_unilever)

# Iterating using for loop - nestle
print('The sales of Nestle and Unilever are in .. Union ')
for val in nestle_unilever_union:
    pprint(val)
print('')
#- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
nestle_unilever_intersection = (countries_nestle & countries_unilever)

# Iterating using for loop - nestle
print('The sales of Nestle and Unilever are in .. Intersection ')
for val in nestle_unilever_intersection:
    pprint('We Are Selling In: ' + val)
print('')

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
nestle_unilever_difference = (countries_nestle - countries_unilever)

# Iterating using for loop - nestle
print('The sales of Nestle and Unilever are in .. difference ')
for val in nestle_unilever_difference:
    pprint('We Are Selling In: ' + val)
print('')

