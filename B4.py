voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
print(voltages)
max_streak = 0
current_streak = 0
start_val = 0
end_val = 0
temp_start = voltages[0]

for i in range(len(voltages) - 1):
    if voltages[i + 1] < voltages[i]:
        if current_streak == 0:
            temp_start = voltages[i]
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
            start_val = temp_start
            end_val = voltages[i]
        current_streak = 0

if current_streak > max_streak:
    max_streak = current_streak
    start_val = temp_start
    end_val = voltages[-1]

duration = max_streak + 1

print("Longest continuous drop:", duration, "minutes Started at:", start_val, "V Ended at:", end_val, "V")
