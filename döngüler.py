#for ve while döngüleri 
sayilar =[1,3,5,7,9,12,19,21]
for sayı in sayilar:
    print(sayı)
isimler=["ayse","sümeyye","hümeyra"]
for isim in isimler:
    print(f"my name is {isim}")
tuple =[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple: #a,b şeklinde olmazza ıkıli yazılmıyor.
     print(a,b) 
name="hümeyra"
for n in name : # harfleri alt alta yazar 
    print(n)   

sayılar=[1,3,5,7,9,12]
for sayı in sayılar:


 while (i<adet):
     name =input("ürün ismi :")

## pc den rastgele sayı ıstedım ve buldurdum 

import random
sayı=random.randint(1,10)
hak=5
sayac=0
while hak>0 :
    hak-=1
    sayac+=1
    tahmın=int(input("tahmınınız:")) 
    if sayı == tahmın:
        print(f"tebrikler {sayac}.defada bildiniz : toplam puanınız {100-(20)*(sayac-1)}")
        break
    elif sayı>tahmın :
        print("yukar")
    else :
            print("asagı: ")
    if hak==0 :
        print(f"hakkınız bitti : tutlan sayı :{sayı}")

########## random.randit(2,100,5 )aralıgında rastegele sayı çetirdim
i=0
sayı=int(input("bir sayı giriniz: "))
asalmı= True
if sayı==1:
    print("1 sayısı asaldegildir: ")           
for i in range(2,sayı):
    if sayı%i==0:
        break
    else:
        print("asal")
