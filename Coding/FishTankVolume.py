length = int(input("Enter the length of the tank in cm:"))
width = int(input("Enter the width of the tank in cm:"))
height = int(input("Enter the height of the tank in cm:"))

volume = length * width * height / 1000
impgal = volume / 4.546

print(f"A {length} x {width} x {height} cm tank is {volume} litres and {impgal} imperial gallons.")