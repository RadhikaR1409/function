def generate_range(a,b,c):
    n=[]
    i=a
    while i<=b:
        n.append(i)
        i=i+c
    print(n)
a=int(input("enter list start number :"))
b=int(input("enter stop number :"))
c=int(input("enter range :"))
generate_range(a,b,c)