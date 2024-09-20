placing = int(input())
ranklist = []
for i in range(placing):
    name, time = input().split()
    ranklist.append((time, name))
ranklist.sort
for position in range(len(ranklist)):
    if ranklist[position][1] == "Percy":
        print(position)