level = float(input("Enter the nitrate level from the test:"))
if level < 1:
    print(f"For {level} nitrate dose 0.5ml of carbon")
elif 1 > level > 2.5:
    print(f"For {level} nitrate dose 1ml of carbon")
elif 2.5 > level > 10:
    print(f"For {level} nitrate dose 2ml of carbon")
else:
    print(f"For {level} nitrate dose 3ml of carbon")
