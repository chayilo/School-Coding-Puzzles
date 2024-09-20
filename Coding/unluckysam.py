word = input():
    if len(word) < 3:
        print("nope")
    
one = word[:2]
two = word[2:]
print(one + "i" + two)