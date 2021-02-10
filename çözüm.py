"""
not1=int(input("1. notunuzu gir: "))
not2=int(input("2.notunuzu gir: "))
not3=int(input("3. notunu gir: "))
ortalama=((not1+not2+not3)/3)
print(ortalama)
if (ortalama>=85):
    print(f"tebrikler takdir belgesi almaya hak kazandınız ortalamanız {ortalama}")
elif ((ortalama<85) and (ortalama>=70)):
    print(f"teşekkür belgesi almaya hak kaznadınız ortalamanız{ortalama}")
else:
        print(f"daha fazla çalışmalısınız :{ortalama}")

# havanın nasıl olduu
hava=input("hava nasıl?")

print(type(hava))
if (hava=="yagmurlu"):
    print("şemsiyeni al :")
elif (hava=="güneşli"):
     print("ince kıyafet giymelisin : ")
else:
    print("havadurumuna dikkatlı bakın! ")

x=5
x=complex(x)
print(x)


age=19
txt="my name is hümeyra,and I am {}"
print(txt.format(age))

print(bool("abc"))
#method özellik deneme
fruits=["apple","banana","chery"]
fruits.append("kiwi")
print(fruits)   #append  eklemek demek methodu ile listeye kivi yi ekledim

fruits.insert(2,"orange") # insert eklemek demek methodu ile istediğim değişkneden sonra ifade ekledim
print(fruits)

print(len(fruits))
fruits.remove("banana") # remove kaldırmak demek istediğim değişkeni kaldırdım
print(fruits) #işlem sonucunda listedeki banana kalktı liste len 1 azaldı
print(len (fruits))


x="computer scene rocks !"
x=45
print(x)
"""
class deneme:
    #class object attribute
    pi=3.14

    def __init__(deger,yarıcap=1):
        deger.yarıcap=yarıcap
    
#methods
def cevre_hesapla(deger):
    return 2*deger.pi*deger