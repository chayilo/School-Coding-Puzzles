mark = int(input("Enter the mark from 0-100:"))
if mark < 2:
    print(f"A mark of {mark} is a Grade U\nYou needed {2-mark} mark(s) to acheive the next grade.")
elif 2 < mark < 4:
    print(f"A mark of {mark} is a Grade 1\nYou needed {4-mark} mark(s) to acheive the next grade.")
elif 4 < mark < 13:
    print(f"A mark of {mark} is a Grade 2\nYou needed {13-mark} mark(s) to acheive the next grade.")
elif 13 < mark < 22:
    print(f"A mark of {mark} is a Grade 3\nYou needed {22-mark} mark(s) to acheive the next grade.")
elif 22 < mark < 31:
    print(f"A mark of {mark} is a Grade 4\nYou needed {31-mark} mark(s) to acheive the next grade.")
elif 31 < mark < 41:
    print(f"A mark of {mark} is a Grade 5\nYou needed {41-mark} mark(s) to acheive the next grade.")
elif 41 < mark < 54:
    print(f"A mark of {mark} is a Grade 6\nYou needed {54-mark} mark(s) to acheive the next grade.")
elif 54 < mark < 67:
    print(f"A mark of {mark} is a Grade 7\nYou needed {67-mark} mark(s) to acheive the next grade.")
elif 67 < mark < 80:
    print(f"A mark of {mark} is a Grade 8\nYou needed {80-mark} mark(s) to acheive the next grade.")
else:
    print(f"A mark of {mark} is a Grade 9\nYou needed 0 more marks to acheive the next grade.")