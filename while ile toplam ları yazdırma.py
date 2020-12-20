#kaça kadra olan sayıların toplamını bulmak istiyorsun
sayi=int(input("kaça kadar toplanmasını istiyorsunuz:"))
sayac=1
toplam=0
while sayi>=sayac:
    toplam+=sayac
    sayac+=1
print(f"{sayi}sına kadar toplamları {toplam}")
