n = int(input("How many resistors? "))
total_resistance = 0

for i in range(1, n + 1):
    r = float(input("Enter R" + str(i) + ": "))
    total_resistance = total_resistance + r

print("Total resistance =", total_resistance, "ohm")
