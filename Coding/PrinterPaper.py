import math as m

numOfSides = int(input())
pagesPerSide = int(input())
singOrDoub = input()
if singOrDoub == 's':
    pages = numOfSides/pagesPerSide
elif singOrDoub == 'd':
    pages = numOfSides/pagesPerSide/2
print(m.ceil(pages))
