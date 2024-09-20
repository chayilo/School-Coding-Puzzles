originalprice = int(input())
if originalprice >= 10:
    newprice = (originalprice*0.8)-4
    print(int(newprice*100))
elif originalprice >= 4 and originalprice < 10:
    newprice = originalprice*0.8
    print(int(newprice*100))
else:
    print(int(originalprice*100))
