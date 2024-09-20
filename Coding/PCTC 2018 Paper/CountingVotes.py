count = 0
numOfLoops = int(input())
yes = 0
no = 0
while count != numOfLoops:
    vote = input()
    if vote == "YES":
        yes += 1
    elif vote == "NO":
        no += 1
    count += 1
print(f"YES {yes}")
print(f"NO {no}")
