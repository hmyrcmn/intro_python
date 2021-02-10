# 100  e kadar olan asal sayıları yazdırmak kendisinden başka böleniolmayan sayılardır

# girilen sayı asalmı
for i in range(5):
    print("merhaba") # 5 kez merhaba yazar

for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)

# 10 a kadar olan sayılarıkaresını
for i in range(0,10,1): # 10 kez döner
    if i %2==1: # tek sayıoalrı bulur
        print(i**2) # tek sayıları yazdırır
    else:
        break
sayı =int(input("sayı: "))
for i in range(0,i<=sayı):
    if (sayı%i==0):
        print("asal değil")
    else :
        print("asaldır")