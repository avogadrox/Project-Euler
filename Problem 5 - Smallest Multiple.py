factors = [20, 19, 18, 17, 16, 14, 13, 11]

for multiple in range (2520, 999999999, 1):
    if all(multiple % factor == 0 for factor in factors):
        print(multiple)
        break
