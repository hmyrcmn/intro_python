# error
while True:
    try :
        x=int(input("1.sayı:"))
        y=int(input("2.sayı:"))
        result=(x/y)
        print(result)
    except Exception as e: #hatanın neden kaynaklandıgının bilgisini verir
        print("yanlış veri girdiniz:",e)
    else:
        break
    finally:
        print("try except sonlandı:")