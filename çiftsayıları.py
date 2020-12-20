
"""
sayi=int(input("kaça kadar çift sayıları yazdıracagını belirt"))
for i in range(0,sayi,1):  # range methods başla,son ,artış miktarı
    if i%2==0:
        print(f"{i}çift sayı")
    else:
        print(f"{i}tek sayı") #for : if:  

#örnek iki
note=int(input("çift sayıları belirt: "))
for i in range(0,note,2):
    print(i) #direk dokuzdan başladıgı için 2 er artmayla yazdı 


##sayı rakam sayacı
msj="benim adım hümeyra ve ilerde çok iyi bir pc müh olacagım 123456789 "
rakam_sayacı=0
harf_sayacı=0
maybe=list(msj) # bu kod str ifardeyi list e yapar
print(maybe)
for i in maybe:
    if str(i).isdecimal(): # rakammı 
        rakam_sayacı+=1
        print(i)
    else:
        harf_sayacı+=1
        print(i)
print("harf sayan " ,harf_sayacı)
print("rakam sayan",rakam_sayacı)


#faktöriyel konusu
x=int(input("faktöriyeli hesaplanacak sayıyı gir: "))
faktöriyel=1
for i in range(1,x+1,1):
    faktöriyel*=i
print(faktöriyel)

"""
#girilen sayıdan bitirilen sayıya kadar sayıları toplayan 
sayı1=int(input("kaçan toplanamaya başlansın :"))
sayı2=int(input("kaça kadar toplansın"))
toplam=0
for sayı1 in range(sayı1,sayı2+1,1):
    toplam+=sayı1
    sayı1+=1
print(toplam)


#sayıın üs kuvvetini alan program yaz
taban=int(input("üssü alınacak sayıyı gir: "))
kuvvet=int(input("kaçıncı kuvvetini almak istiyorsun: "))
sonuc=1
for i in range(1,kuvvet+1,1): #kaç kez bu işlemi yapacagını belitir yani üss kaç ise for döngüsüde o kadar olmalı ki asagıda o kadra çarpım yapılsın
    sonuc*=taban
print(sonuc)


#fonksiyonlarda liste halinde çift sayıları yazdır
def çift_sayılar(sayı):
    liste=[]
    for i in range(1,sayı,1):
        if i%2==0:
            liste.append(i)
    return liste
print(çift_sayılar(10))
