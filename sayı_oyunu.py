import random
random_sayı=random.randint(0,100)
tahmin=int(input("tahmn: "))
    if tahmin ==random_sayı:
         print("tebrikler sayıyı buldunuz")
         
    elif tahmin>random_sayı:
        print("aşagı")
    else:
        print("yukarı") 