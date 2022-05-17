import math
def printitem(array:dict):
    ''' print product and sale in dict '''
    for product,sale in array.items():
     print(product, ":", sale ,"US Dollars")

def topSelling(array):
    ''' print max sale '''
    maxNe=max(array)
    print("highest selling product is:",maxNe ,"and price is", array[maxNe],"\n")

def printSet(array):
    ''' print iteam in set by using loop'''
    for i in array:
        return array

# creat dic 
nestleProducts={"kitkat": 34456432, "nescafe":14106132, "maggi": 9960312, "nido":44506003}
unileverProducts={"lipton":23456000, "bereyers":1235891, "hellmanna":17241412, "marmite":11715324}

# print products and sales for companies
print("Nistle products and sales figures :")
printitem(nestleProducts)
print("\nUnilever products and sales figures :")
printitem(unileverProducts)

# which companies has more products
if len(nestleProducts.keys()) > len(unileverProducts.keys()):
    print("Nestle Have More Products")
if len(nestleProducts.keys()) < len(unileverProducts.keys()):
    print("Unilever Have More Products")
else:
    print("\nBoth Companies You Have The Same Number Of Products\n")

# top selling product
print("Nestle",end=" ")
topSelling(nestleProducts)
print("Unilever",end=" ")
topSelling(unileverProducts)


nestleCities={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileverCities={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

# print all the cities
print("Nestle Citites is: ",printSet(nestleCities))
print("Uniliver Citites is: ",printSet(unileverCities))

# common cities by using loop
intersect = nestleCities.intersection(unileverCities)
print('Nestle & Unilever:')
for i in intersect:
    print(i,end=" ")

# cities in Nestle and not in Unilever by using loop
symmetric_difference = nestleCities.difference(unileverCities)
print('\nNestle - Unilever: ')
for i in symmetric_difference:
    print(i,end=' ') 




