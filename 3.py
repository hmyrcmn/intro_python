#faktöriyel hesaplama
sayi=int(input("faktörüyeli hesaplanavak sayıyı gir: "))
sayac=1
carpım=1
while (sayi>=sayac): 
    carpım*=sayac
    sayac+=1
    
print(f"{sayi} sının faktüriyeli {carpım}")    