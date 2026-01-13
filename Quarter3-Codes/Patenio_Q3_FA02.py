import numpy as np

names = ["Me", "Lia", "Jake"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])
for i in range(len(names)):
    print(names[i], steps[i])