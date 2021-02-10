def yazdır(kelime,adet):
    print(kelime  * adet)
    
yazdır("merhaba\n",5)     ####birşeyi belirtilern kadar nasıl yazılır :

def listeye_cevirme(*args): # * sınırsız sayıda veri girilecegini belirtir
liste=[]

for arg in args :
    liste.append(arg)

return liste
result=listeye_cevirme(10,20,"rnfjknrkjfnrek",3,"jrnfjrfnujhurhur")
print(result)