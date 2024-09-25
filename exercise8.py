a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

d = list(zip(a,b,c))

for s in d:
    z=0
    for v in s:
        z+=v
    print(z)