import numpy as np

names = ["Me", "Lia", "Jake"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

for i in range(len(names)):
    total_steps = np.sum(steps[i])
    avg_steps = np.mean(steps[i])
    min_steps = np.min(steps[i])
    max_steps = np.max(steps[i])
    print(
        f"{names[i]} - Total Steps: {total_steps} | "
        f"Average: {avg_steps:.1f} | "
        f"Min: {min_steps} | Max: {max_steps}"
    )