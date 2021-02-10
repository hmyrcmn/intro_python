x=int(input("x degeri :"))
y=int(input("y degeri: "))

liste_tuple=(x,y)
print(liste_tuple)

 
if (x<5 and x>-5) and (y<5 and y>-5):
    print("çemeber içinde")
 
elif (x==5 or x==-5) and (y==5 or y==-5):
    print(" çember içinde")

else:
    print("çember dişinda ")