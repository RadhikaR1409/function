def str_num():

    a=[]
    size=int(input("enter the size of list"))
    i=1
    while i<=size:
        element=input("enter the list element :")
        a.append(element)
        i=i+1
        print(a)

    length=len(a)

    count=0
    j=0
    while j<length:
        if len(a[j])>1:
            length1=len(a[j])
            # k=0
            # while k<length1:
            if a[j][0]==a[j][length1-1]:
                count=count+1
                print(a[j])
            #     else:
            #         print("last element not equal")
            # else:
            #     print("len is less than 1")
            # k=k+1
        j=j+1

    print(count)

str_num()
            

