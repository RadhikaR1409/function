def multiple_sum(limit):
    sum=0
    i=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
            print(i)
        i+=1
    print(sum)

limit=int(input("enter the limit : "))
multiple_sum(limit)

