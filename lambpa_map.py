# lambda and map methodları nasıl kullanılır örnekleyelim

def kac_basamak(num): 
    if 10**1<=num<10**2:
        print("1 basamaklı")
    elif 10**2<=num<10**3:
        print("2 basamaklı")
    elif 10**3<=num<10**4:
        print("3 basamaklı")
    else:
        print("fazla basamaklı")
liste=[1,12000,2300,22,4000,110,100,120]
result=list(map(kac_basamak,liste))
print(result)

print("*****",help(kac_basamak))

# def square(num): return num**2

numbers=[1,2,3,4,5,6,7,8,9,10]
# result=list(map(square,numbers))
result=list(map(lambda num: num **2,numbers))
print(result)
square=lambda num: num **2
result=square(100) # def yapmadan lamda yı fon gibi kullandım ve çalıştı
print(result)

"""
NOTE
DEF OLMADAN DA O İŞLEMİ YAPAN LAMDA VAR SADECE PARAMETRE ATAMALI VE O PARAMAETRE İLE NE YAPACAGI SÖYLENMELİ 
MAP : İLE LİSTEDEKİ İFADELERİ TEK TEK FOR YAPMADAN ELDE EDERİM
LİST: İLE MAP DEN GELEN DEGERLEİR LİSTEYE ATARIM VE SONUCU LİSTE OLARAK DÖNDÜRÜRÜM
"""