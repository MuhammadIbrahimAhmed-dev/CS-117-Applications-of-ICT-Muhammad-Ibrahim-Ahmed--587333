def loaded_divider(vs, r1, r2, rL):
    # Parallel equivalent of r2 and rl
    r_parallel = (r2 * rL) / (r2 + rL)
    
    # Unloaded theoretical voltage
    unloaded_v = vs * (r2 / (r1 + r2))
    
    # Actual loaded voltage
    loaded_v = vs * (r_parallel / (r1 + r_parallel))
    
    return unloaded_v, loaded_v

result = loaded_divider(12, 1000, 1000, 500)
print("Loaded Voltage Divider Results:", result)
