message = "CHAYIL"
offset = 0
data = []
for c in message:
    c = ord(c)
    c = (c + offset)
    if c > 122:
        c -= 26
    if 91 < c < 97:
        c += 26
    data.append(chr(c))

print("".join(data))
    
    

