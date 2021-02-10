
#file=open("dosyaislemleri","w",encoding="utf-8") # yazmak için dosya açtı olmayan dosyayıda açar

# w= dosya yaz  olmayan dosyayı olustur önceki yazılanlar siler
# file=open("dosyaislemi.txt" ,"r+" ,encoding="utf-8")
# file.write("hello")
# print("file")
# file.close()
#file=open("dosyaislemleri.txt","x",encoding="utf-8")

with open("dosyaislemleri.txt","w",encoding="utf-8") as file:
    print(file.write("hello\n"))
    file.write("hümeyra çimen\n")
    file.write("hümeyra çimen\n")
    file.write("hümeyra çimen\n")
    file.write("hümeyra çimen\n")
    file.write("hümeyra çimen\n")

    print(file.tell())
    file.seek(30)
    file.write("123456789")
    with open("dosyaislemleri.txt","r+",encoding="utf-8") as file:
        list=file.readlines()
        print(list)
        print(list[2])
        for i in list:
            print(file.write(i))

    print(file)