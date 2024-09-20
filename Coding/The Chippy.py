fish = int(input())
chips = int(input())

cost = fish*5 + chips*2
if cost > 20:
    yayornay = input()
    if yayornay == "y":
        print(f"{cost + 1}")
    else:
        print(cost)
else:
    print(cost)