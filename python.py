#Git verkefni forritun

#Dæmi 1

tala1=int(input("Sláðu inn tölu "))
tala2=int(input("Sláðu inn tölu "))
tala3=tala1+tala2
tala4=tala1*tala2
print("Lagðar samana=",tala3)
print("Margfaldaðar=",tala4)

#Dæmi 2

nafn1=input("Fornafn: ")
nafn2=input("Eftirnafn: ")
print("Nei, góðan og blessaða daginn",nafn1,nafn2)


#Dæmi 3
upper=0
lower=0
oft=0
hogl=0
texti=input("Sláðu inn texta ")
for i in (texti):
    if i.isupper():
        upper+=1
        if texti[oft+1].islower():
            hogl+=1
    if i.islower():
        lower+=1
    oft+=1
print(upper,"Hástafir")
print(lower,"Lágstafir")
print(hogl,"Lágstafir strax á eftir hástöfum")
