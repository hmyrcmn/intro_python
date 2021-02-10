fruits={"apple ","banana","orange"}

print(fruits[0]) #indekslenemez

for x in fruits:
    print(x)

fruits.add("mango")
fruits.update(["chery","grape"])

for x in fruits:
    print(x)
print(fruits)

mylist=[1,2,3,2,1,1,1,1,1,11,1]
print(mylist)
print(set(mylist))   # set methods tekrarlanan sitringleri yazmaz tek seferlik yazar


print(fruits)
fruits.remove("mango") #siler 
print(fruits)
fruits.discard("grape") #siler
print(fruits)

value sitring number y yi x e atadıktan sonra y de yaptıgım değişiklik x i etkilemez
x=4
y=90
x=y
y=78
print(x,y) 
referens list atamadan sonra yapılan değişiklik etkiler 2 aynı liste olur
a=["apple ","banana"]
b=["grape"]
a=b #sonucta neden a grape olmadı nın cevabı
b[0]="chery"
print(a,b)

x,y,z,=2,5,7

numbers=1,5,7,10,6

a=int(input("1.sayı: "))
b=int(input("2. sayı: "))
result=(a*b)-(x+y+z)
print(result)

sayı1=input("birinci  sayı giriniz: ")
sayı2=input("ikinci sayı giriniz: ")
print(type(sayı1))
sayı1=int(sayı1)
sayı2=int(sayı2)
print(type(sayı1))
print(type(sayı2))
toplam=x+y+z
carpım=sayı1*sayı2
fark=carpım-toplam
print(fark)

y nin x e kalansız bolumu // ile yapılır kısa yol
result=y//x
print(result)

bolum=y/x
print(int(bolum))
print(float(bolum))

x,y,z, toplamının mod 3 u ne
toplam=(z+y+z)
result=toplam%3
print(result)

uss=y**x
print(uss)
*********** x,,*y, znumbers içine ata z nini küpünüal 
numbers=1,5,7,10,6
x,*y,z=numbers
print(x,y,z)
result=z**2
print(result)
toplu_y=y[1]+y[2]+y[0]
print(toplu_y)
******************************************
adınız=input("adınız: ")
yas=int(input("yasını: "))
egitim=input("egitim: ")

koşul ifadeli ehliyet alıp alamama kodu :D herkes uyudu kod yazıyom :(
if (yas>=18) :
    if (egitim=="lise")or( egitim=="lisans"):
        print(f"{adınız } ehliyet alabilirsiniz")
    else :
         print(f"{adınız} ehliyet egitimin yetersiz")
else :
     print(f"{adınız} ehliyet alamıyorsunuz yaşnız yetmiyor")
    ********************************************************************


yazılı1=float(input("1. yazılı: "))
yazılı2=float(input("2. yazılı: "))
sozlu=float(input("sozlu: "))
ortalama=(yazılı1+yazılı2+sozlu)/3
x=ortalama
if (x>=0)and(x<=24) :
    print(f"ortalamanız: {ortalama} notunuz: 0")
elif (x>=25)and(x<=50):
    print(f"ortalamanız: {ortalama } notunuz")

numbers= [1,2,3,4,5]

for a in numbers :
    print(a)

names=["hümeyra","ayşe","sumeyye"] 
for name in names :
    print(f"my name is {name} .")
name=("hümeyra")
for a in name :
    print (name)

tuple =[(1,2),(3,4),(3,5)] # hepsi parantezli olmalı 
for a,b in tuple:
    print (a,b)
d={"k1":1,"k2":2,"k3":3}
for ıtem in d.items() :
    print(item)   """

sayılar =[1,3,5,7,9,12,19,21]

for sayı in sayılar:
    if sayı%3==0:  # lisatede 3 e bölüne bilen sayıları yazar
        print(sayı)

toplam=0
for sayı in sayılar:
    toplam += +sayı    # listedeki elemanları tek tek toplar 
    print(toplam)
"""
sayılar =[1,3,5,7,9,12,19,21]
tek sayıların karesını al 
for sayı in sayılar:
    if sayı%2==1:
        kare=sayı**2
        print(kare)

urunler =[
    {"name":"samsung s6","price":"3000"},
    {"name":"samsung s7","price":"4000"},
    {"name":"samsung s8","price":"5000"},
]
toplam =0
for urun in urunler :
    fiyat=int(urun["price"])
    toplam+=fiyat
print(toplam)    

sayılar=[1,3,5,7,9,12,19,21]
x=True
while x:
    print(sayılar)
    






