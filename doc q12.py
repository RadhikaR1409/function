def remove_zero(a):
    #a=int(input("enter any number :"))
    while a>0:
        rem=a%10
        if rem>0:
            print("number without zero is ",a)
            break
        a=a//10
n=int(input("enter any number :"))
remove_zero(n)









def remove_zero():
    a=int(input("enter any number :"))
    while a>0:
        rem=a%10
        if rem>0:
            print("number without zero is ",a)
            break
        a=a//10
remove_zero()









