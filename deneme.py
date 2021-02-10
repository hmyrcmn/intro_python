markalar=[]
input("marka:  ")
markalar.append(input)
# print(markalar)

list =['ali','veli']
tuple=("damla" ,"deniz")
print(type(list))
print(type(tuple))# list ve tuple benze mantıkta çalışır 
print(list[0])
print(tuple[1]) #list ler gibi değişkeni secebiliriz fakat
list[1]="zeki"
print(list) #değişkeni değiştirdi ama tuple değiştirmez
# tuple[1]="ezgi"


users={

    "name":"hümeyra",
    "surname":"çimen",
    "age":19,
    "addres":"kayseri",
    "abbility":"just student",
}


print(users)
print(users["name"])
print(users["age"])

