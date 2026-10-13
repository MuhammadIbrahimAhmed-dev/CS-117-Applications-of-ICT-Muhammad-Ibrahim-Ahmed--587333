readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
print(readings)
above_count = 0
total_sum = 0
highest = readings[0]
lowest = readings[0]

for val in readings:
    
    if val > 3.2:
        above_count += 1
        
    if val > highest:
        highest = val
        
    if val < lowest:
        lowest = val
        
    total_sum += val

average = total_sum / len(readings)

print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", average, "V")
