def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r

v_val = 12
r_val = 6

current = ohms_current(v_val, r_val)
power = power_dissipated(current, r_val)

print("Current =", current, "A")
print("Power =", power, "W")
