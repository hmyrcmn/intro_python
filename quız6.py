def ucgenmi(a,b,c):
    if (b-c)<0:
        if (c-b)<a<(b+c):
            print("ücgendir")
        else :
            print("üçgen olmaz")
    else:
        if (b-c)<a<(b+c):
            print("üçgendir")
        else:
            print("üçgendeğil")

a=int(input("a değeri:"))
b=int(input("b değeri:"))
c=int(input("c değeri:"))
ucgenmi(a,b,c)