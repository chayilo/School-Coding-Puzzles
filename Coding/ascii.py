import math

PPI = int(input("What is the PPI?"))
width = float(input("What is the width of the image in inches?"))
height = float(input("What is the height of the image in inches?"))
colours = int(input("How many colours could be in each pixel?"))
colourdepth1 = math.log2(colours)
colourdepth2 = math.ceil(colourdepth1)
bits = print(f"The total amount of bits in this image is, {(height*PPI)*(width*PPI)*colourdepth2}")
print(f"In KiB: {bits/8/1024}")
print(f"In MiB: {bits/8/1024/1024}")
print(f"In GiB: {bits/8/1024/1024/1024}")
