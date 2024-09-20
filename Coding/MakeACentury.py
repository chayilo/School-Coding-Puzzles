a = int(input())
b = int(input())

c = (a+b)
d = (b-a)
e = (a-b)

if c > d and c > e:
    print(abs(100-c))
    
elif d > c and d > e:
    print(abs(100-d))
    
elif e > d and e > c:
    print(abs(100-e))