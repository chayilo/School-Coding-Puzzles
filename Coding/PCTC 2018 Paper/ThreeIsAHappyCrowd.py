a = int(input())
b = int(input())
c = int(input())
e = a+b
f = a+c
g = b+c
if e == a or e == b or e==c:
    print("HAPPY CROWD")
elif f == a or f == b or f==c:
    print("HAPPY CROWD")
elif g == a or g == b or g==c:
    print("HAPPY CROWD")
else:
    print("UNHAPPY CROWD")