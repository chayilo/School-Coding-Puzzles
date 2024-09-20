import statistics as stats

arr = []
while True:
    inp = input("What is your number?")
    if inp == "e":
        break
    num = float(inp)
    arr.append(num)

print("Total: ",sum(arr))
print("Top: ",max(arr))
print("Bottom: ", min(arr))
print("Average: ",stats.mean(arr))