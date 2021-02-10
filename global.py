"""
name="ayşe"
def change_name(newname):
    name=newname
    print(name)

change_name("hümüş") #sadece fon. da geçerli olur dişardaki sabittir
print(name) #def fonk dışardaki name i etkilemedi  AMA GLOBAL OLUNCA DEĞİŞİR

###############
x=80
def change_num(newnum): # new num yerine yazılan ifade fonksiyon içinde x e atanır
    global x
    x=newnum
    print(x)

print(x) #x in fonk dışındaki degeri global olan
change_name(9000)

"""
##########################################################
"""
humeyraHesap={
    'ad':'hümeyra çimen',
    'hesap no':'3456',
    'bakiye':3,
    'ekhesap':1
}
ayseHesap={
    'ad':'ayşe çimen',
    'hesap no':'17890',
    'bakiye':5,
    'ekhesap':2
}
def paracek(hesap,miktar):
    print(f"merhaba  {hesap['ad']} ")

    if hesap['bakiye'] >=miktar:
        hesap['bakiye']-miktar
        print(f"{hesap['ad']} paranızı çekebilirsiniz ")

    else:
        toplam=hesap['bakiye'] +hesap['ekhesap']
        if toplam>=miktar:
            ekhesapkullanımı=input("ek hesapdan para cekmek istermisiniz e/h")
            if ekhesapkullanımı=='e':
                print("paranızı alabilirsiniz")
                
            else:
                print(f"{hesap['hesap no']} hesabınızda {hesap['bakiye']} niz bulunmaktadır")
        else:
            print(f"{hesap['hesap no']} nolu hesabınızda bakıyenız yetersız")    




#paracek(ayseHesap,5)
paracek(ayseHesap,7)
#################################################################################################
"""
"""
def swap(x,y):
    return y,x

x=3
y=5
print(x,y)
print(swap(x,y)) # SWAP ÖZELLİĞİ İLE FONKSİYON ULLANARAK YER DEĞİŞTİRDİM

#################################################
"""


# BİRDEN 10 A KADAR OLAN SAYILRIN TOPLAMINI YAZDIR
"""
toplam=0
for i in range(1,10,1) :  # 9 kez döngü döner
    toplam+=i 
    

print(toplam) # 1+.........9=45 
"""
i=1
toplam=0
while i<10:
    toplam+=i
    i+=1
print(toplam)