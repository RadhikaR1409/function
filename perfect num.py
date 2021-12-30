def perfect_num():
    num=int(input("enter any number :"))
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print("this is a perfect number")
    else:
        print("not a perfect number")

perfect_num()
