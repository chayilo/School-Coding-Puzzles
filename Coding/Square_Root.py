x = int(input("Enter a number:"))
root = x
while root != 0.5 * (root + (x / root)):
    print(0.5 * (root + (x / root)))
    root = 0.5 * (root + (x / root))