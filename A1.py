v = float(input("Enter voltage (V): "))
r = float(input("Enter resistance (ohm): "))

if r <= 0:
    print("Invalid resistance")
else:
    current = v / r
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
