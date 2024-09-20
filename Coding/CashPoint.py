cash = int(input("Enter the amount to withdraw: £"))
print(f"W{cash}")
while cash >= 20:
    print("D20")
    cash = cash-20
while cash >= 10:
    print("D10")
    cash = cash-10
while cash >= 5:
    print("D5")
    cash = cash-5
