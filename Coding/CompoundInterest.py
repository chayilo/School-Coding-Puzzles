balance = int(input("Enter the balance to the nearest pount: £"))
rate = int(input("Enter the % interest rate:"))
tbalance = int(input("Enter the target balance to the nearest pound: £"))

year = 1

while balance * (100+rate)/100 < tbalance:
    balance = balance * (100+rate)/100
    print(f"Year {year}: Balance is £{balance}")
    year = year + 1
print(f"Year {year}: Balance is £{balance*(100+rate)/100}")