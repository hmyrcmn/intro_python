liste1=[1,3,5,7,9,11]
liste2=[2,4,6,8,10]
liste3 =liste1+liste2 # iki diziyi birleştirdim

print(liste3)

temp=[]
for i in liste3:
    # liste3[x]=(i*2)
    i=i*2
    temp.append(i)
    
for x in temp:
    if x%2==0:
        print("çift")
    else :
        print("tek")

print(temp)   
for x in temp :
    print(type(x))