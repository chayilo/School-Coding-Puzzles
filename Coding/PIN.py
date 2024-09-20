pin = 7528
counter = 0

while counter < 3:
    userpass = int(input())
    if userpass == pin:
        print("Security check passed.")
        counter += 100
    else:
        print("Locked out.")
        counter += 1