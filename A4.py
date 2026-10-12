a = int(input("Enter bit A (0 or 1): "))
b = int(input("Enter bit B (0 or 1): "))

if a != 0 and a != 1:
    print("Bits must be 0 or 1")
elif b != 0 and b != 1:
    print("Bits must be 0 or 1")
else:
    if a == 1 and b == 1:
        print("AND output = 1")
    else:
        print("AND output = 0")

    if a == 1 or b == 1:
        print("OR output = 1")
    else:
        print("OR output = 0")

    if a != b:
        print("XOR output = 1")
    else:
        print("XOR output = 0")
