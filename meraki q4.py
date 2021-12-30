def show_num(limit):
    
    i=0
    while i<=limit:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i+=1


limit=int(input("enter the limit :"))
show_num(limit)