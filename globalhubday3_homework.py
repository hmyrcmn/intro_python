cv={}
kac_kisi=int(input("kaç kişi için cv girişi yapacaksınız ! "))
for i in range(0,kac_kisi,1):
    ıd= int(input("öğrenci no: "))
    name = input("öğrenci adı: ")
    surname = input("öğrenci soyad: ")
    phone = input("öğrenci telefon: ")
    salary=int(input("maas : "))
    cv.update({
        ıd: {
            'ad': name,
            'soyad': surname,
            'telefon':phone ,
            'maas':salary
        }
    })

print("bilgisini almak istediğiniz kişinin ıd sini giriniz ! ")
ıd =int( input('öğrenci no: '))
employee = cv[ıd]
print(employee)