def str_case():
    str1=input("enter the string :")
    lower=0
    upper=0
    space=0
    i=0
    while i<len(str1):
    #for i in str1:
        if (str1[i]).islower():
            lower=lower+1
            
        elif (str1[i]).isupper():
            upper=upper+1
            
        else:
            space=space+1
            print(space,i)
        i+=1

    print("lower are :",lower)
    print("upper is :",upper)
        
str_case()