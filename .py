z=[1,2,3,1]
d=[]
for i in z:
    if d.count(d)==0:
        d.append(i)
        if d.count(i)>1:
            d.append(i)
            print(d)
