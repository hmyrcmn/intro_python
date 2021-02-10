file=open("once.txt","w",encoding="utf-8")
file.write("Bursa Teknik")
print(file)

file=open("once.txt","w",encoding="utf-8")

i=1
while i<13:
    file.seek(1)
    file.write(" ")
    i+=1
print(file)
file=open("once.txt","r",encoding="utf-8")
liste=file.readlines()
file2=open("sonra.txt","w",encoding="utf-8")
for i in range(0,i<26):
    for i in range(0,i<26):
        liste[i]=file2.append(liste[i])
