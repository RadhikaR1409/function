def unique_ele(list1):
    list2=[]
    i=0
    while i<len(list1):
        if list1[i] not in list2:
            list2.append(list1[i])
        i=i+1
    print(list2)
#list1=[1,2,3,3,3,4,4,5,6,7]
unique_ele(list1=[1,2,2,3,3,3,4,5,6,7,8,8,8,9,0])