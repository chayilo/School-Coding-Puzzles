value = int(input("Enter the value of the car purchased: £"))
PEV = int(input("Enter the minimum part exchange value: £"))
year = 0
depreciation = 0.75


while value * 0.75> PEV:
    print(f"In year {year} the car is worth £{value}")
    year = year + 1
    value = value * depreciation
print(f"Part exchange before the end of year {year}")