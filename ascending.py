a=[3,5,2,7,4]
a1=[]
i=0
while i<len(a):
    temp=a[i]
    j=0
    while j<len(a):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

            a1.append(a[i])
        j=j+1
    i=i+1
print(a1)







a[10,20,30,40,50]
b=[100,200,300,400,500]
temp=a[i]
i=0
while i<len(a):
    j=5
    while j<len(b):
