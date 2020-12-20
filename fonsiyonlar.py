
def deMerhaba(ad="user"):
    print("merhaba" + ad)
deMerhaba()
deMerhaba("AYŞE")
deMerhaba("hümeyra")

def sayhello(name="user"):
    return "hello "+ name

msg=sayhello("sümüş")
print(msg)
sayhello("sümeyye") # bu ifade yazılmadı 


def yashesapla(dogumyılı,isim):
    return str(2020-dogumyılı) +isim

age=yashesapla(2001, " hümeyra")
print(age)

def yaskac(dogumyılı):
    return 2020-dogumyılı 
    dogumyılı.append(isim)

yas=yaskac(2001)
yas=yas.append("hümeyra")
print(yas)


def sayHello(name):
    return "hello" +name
msj=sayHello("hümeyra")
print(msj)




# def emekliligekacyılkaldı(yashesapla,isim):
#     yas=yashesapla(dogumyılı,isim)
#     emeklilik=65-yas
#     if emeklilik>0:
#         print(f"emekliliginize {emeklilik} yıl kaldı")
#     else:
#         print("zaten emekli oldunuz")

# print(help(emekliligekacyılkaldı))
# emekliligekacyılkaldı(2001,"hümeyra")

# BELİRTİLEN İFADEYİ BELİRTİLEN KEZ EKRANDA NASIL YAZDIRIRIM
def yazdır(kelime,adet):
    return (kelime*adet)
print(yazdır("adım hümeyra\n",19))               

# for ile yapmaya çalışalım :
kelime=(input("kelime: "))
adet=int(input("kaç kez : "))
for i in range(1,adet+1,1): # for koşul sayısı kadar döner
    print(kelime)

# birde while ile denesem 
kelime=input("kelime:")
adet=int(input("adet: "))
sayac=0
while sayac<adet:
    print(kelime)
    sayac+=1


# sınırsızz ifadeyi alıp liste içine alan bir fonksiyon yaz
def listeye_cevir(*params) : #*args yapmam sınırsız ifade verilecegini belirtir
    liste=[]
    for param in params:
        liste.append(param)
    return liste    
sonuc=listeye_cevir(1,2,3,4,"fjnvjfnvjnf")
print(sonuc)

#İKİ SAYI ARASINDDAKİ ASAL SAYILARI NASIL YAZIDIRIZ 

def asallarıbul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1,1):
        if sayi>1:
            for i in range(2,sayi,1): # sayı eklemedilk 
                if sayi % i==0: 
                    break
            else:
                print(sayi)
    

sayi1=int(input("sayi1: "))
sayi2=int(input("sayi2: "))
asallarıbul(sayi1,sayi2)

#göndeilen sayının tam bölenlerini ekrana yazdır
sayı=int(input("sayı: "))
def tambölenleribul(sayı):
    tambolenler=[]
    for i in range(1,sayı+1,1):
       if sayı%i==0:
           tambolenler.append(i)
    return tambolenler

print(tambölenleribul(22))
"""
def check_even(num):return num%2==0
numbers=(1,2,3,4,5,6)
result=list(filter(lambda num: num%2==0,numbers)) #FİLTER FİLTERELEM GİBİ SADECE ÇİFT LERİ LİSTEDE YAZDI
print(result)
