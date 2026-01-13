import numpy as np

names = ["Me", "Lia", "Jake"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

total_steps = np.sum(steps, axis=1)

for i in range(len(names)):
    print(f"{names[i]} - Total Steps: {total_steps[i]}")

max_steps = np.max(total_steps)
min_steps = np.min(total_steps)

max_index = np.argmax(total_steps)

print(f"\nHighest Total Steps: {names[max_index]} ({max_steps})")
print(f"Difference between highest and lowest total: {max_steps - min_steps}")