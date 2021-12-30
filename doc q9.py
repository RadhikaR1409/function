def list_ele_sqr(a,b):
    c=[]
    i=0
    while i<len(a):
        c.append(a[i]**2)
        #print(c)
        i+=1
    j=0
    while j<len(b):
        c.append(b[j]**2)
        #print(c)
        j+=1
    print(c)
x=[1,2,3,4,5]
y=[30,29,28,27,26]

list_ele_sqr(x,y)

