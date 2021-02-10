

result=bul(10):
print(result)
def bul(i):
    for i in range(1,10,1):
        depo=[]
        if(i%2==0):
            result=(i/2)
            if (result==1):
                depo.append(i)
            else :
                bul(i)
        else:
            result=3*i+1
            if result==1:
                depo.append(i)
            else :
                bul(i)
        
