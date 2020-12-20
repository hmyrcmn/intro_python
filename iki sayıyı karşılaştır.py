#iki sayıyı karşılaştırma oyunu:)
"""
sayi1=int(input("sayı giriniz:"))
sayı2=int(input("2.sayıyı gir:"))

if (sayi1>sayı2):
    print(f"{sayi1} buyuktür {sayı2} den ")
elif (sayi1<sayı2):
    print(f"{sayı2} büyüktür {sayi1}den")
else :
    print("iki sayı eşittir:")
"""
# 3 sayı arasından en büyüğü yazdır 
sayi1=int(input("1. sayyıy gir"))
sayi2=int(input("2. sayı gir:"))
sayi3=int(input("3. sayı gir :"))
if (sayi1<sayi2) and sayi2>sayi3 :
    print(f" en büyük sayı: {sayi2} ")
elif (sayi1>sayi2) and (sayi1>sayi3):
    print(f" en büyük sayı: {sayi1}")
elif sayi2==sayi1 and sayi1==sayi3:
    print("sayılar eşittir:")
else :
    print(f"{sayi3} en büyük sayı")

