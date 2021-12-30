def licence(speed):
    if speed>=70:
        speed=speed-70
        rem=speed//5
        print("your point=",rem)
        if rem>12:
            print("your license suspended :")
    else:
        print("ok")

speed=int(input("enter the speed : "))
licence(speed)



        