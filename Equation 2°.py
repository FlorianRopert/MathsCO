from math import *
a = float(input("Entrez a"))
b = float(input("Entrez b"))
c = float(input("Entrez c"))
delta= b**2-4*a*c
if delta ==0 :
    print((-b)/(2*a))
elif delta >0:
    print((-b+sqrt(delta))/(2*a) , (-b-sqrt(delta))/(2*a))
else:
    print(None)



