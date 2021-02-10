message="HELLO there. my name is hümeyra çimen"

# message=message.upper() #değişken içindeki tüm harfleri BÜYÜK yapar 
# message=message.lower() #değişken içindeki tüm harfleri KÜÇÜK yapar
# message=message.title()  # değişken içindeki tüm kelimelerin ilk harflerini BÜYÜK yapar
# message=message.capitalize() # sadece ilk kelimenin ilk harfini büyük yapar 
# message=message.strip() #baştaki boşluğu yok eder
# message=message.split() #kelimeleri ayırır
# message=" ---".join(message) # split de ayrılan kelimeleri istediğin şekilede birleştirir
# isfound=message.startswith("H") #ile başlıyormu diye sorar boll türünde
# isfound=message.endswith("n") #ile bitiyormu sorusu boll türü cevap
# print(isfound)
# index=message.find("hümeyra")# bull varmı  varsa 0 1 gibi index no söyler
# index=message.find("****") # yoksa -1 değerini verir 
# print(index)
# message=message.replace('hümeyra','hümüş') # değiştirir 
# message=message.replace("ç","c") .replace("ü","u")



# key value ile yazılır  
 
number=input("ögtenci no :")
name=input("ogrenci ad:")
surname=input("ogrenci soyad:")
phone=input("ogrenci telefon:")
 ogrenciler={}
 ogrenciler=[number]={
     "ad":name,
     "soyad":surname,
     "telefon":phone,
 }

# ogrenciler.update({
#     number:{
#         "name":ad,
#         "surname":soyad,
#         "phone":telefon,
#     }
# })

print(ogrenciler)
print(0xAA)