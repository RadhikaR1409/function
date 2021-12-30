def sheep():
    a=['true','true','true','false','true','true','true','true','true','false','true','false']
    count=0
    i=0
    while i<len(a):
        if a[i]=='true':
            count=count+1
            return count
        i=i+1
    print("number of sheeps are ",count)
sheep()