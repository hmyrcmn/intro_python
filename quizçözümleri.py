"""
plakakodu=int(input("kod gir:"))
if plakakodu==34:
    print("istanbul")
elif plakakodu==16:
    print("bursa")
elif plakakodu==17:
    print("çanakkale")
else :
    print("bizim belirledigimiz aralıkta değil!\n lütfen başka bir deger girin ")
"""
"""
sehirler=["izmir","istanbul","bursa","kayseri","çorum"]
for sehir in sehirler:
    lenght=len(sehir)
    son=sehir[lenght-2:lenght:1]
    # print(son)
    bas=sehir[0:2:1]
    print(bas,son)
"""
print("3 il kodu gir")

for  i in range (3):
    dizi=[]
    ilk=int(input("1.kod"))
    dizi.append(ilk)
    
print(dizi)
a=int(input("sayı 1:"))
b=int(input("sayı 2: "))

for i in (a,b+1,1):
    print("y=",i**2+3*i-4)