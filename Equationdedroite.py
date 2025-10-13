AbscissePa = int(input("Entrez xa oui"))
OrdonnéePa = int(input("Entrez ya"))
AbscissePb = int(input("Entrez xb"))
OrdonnéePb = int(input("Entrez yb"))
CoefDirect = (OrdonnéePb-OrdonnéePa)/(AbscissePb-AbscissePa)
OrdoOrig= OrdonnéePa-CoefDirect* AbscissePa
print(CoefDirect,"x+",OrdoOrig)
