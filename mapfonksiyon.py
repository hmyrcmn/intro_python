
def square(num): 
    return num**2

result=square(3) #yazılan sayının karesını alır 
print(result)

def square(num):return num**2

numbers=[1,2,3,4,5,6]
result=list(map(square,numbers)) # bu özellik MAP belirtilen fonksiyonu liste içine atar
print(result) #LİSTE ŞEKLİNDE YAZDIRIR SONUÇALRI

for i in map(square,numbers): # MAP özelliği ni kullandık for döngüsüyle yazdı
    print(i) # SONUÇLAR ALT ALTALTA YAZILIR

    # LAMbDA ÖZELLİĞİ 
numbers=[1,3,5]
square=lambda numbers : numbers**2
result=list(map(square,numbers))
print(result)


#LAMBDA DENEME
def square(num):return num**2
numbers=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda num: num**2,numbers))
print(result)

#filter özelliği
def check_even(num):return num%2==0
numbers=(1,2,3,4,5,2324)
result=list(filter(check_even,numbers))
print(result)

def check_even(num):return num%2==0
numbers=(1,2,3,4,5)
result=list(filter(lambda num: num%2==0,numbers))
print(result)


