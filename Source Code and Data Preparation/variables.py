import numpy as np

next_2weeks_dates = []
for i in range(1, 9 + 1):
    next_2weeks_dates.append(f"2016-07-0{i}")
for i in range(10, 14 + 1):
    next_2weeks_dates.append(f"2016-07-{i}")

next_2weeks_dates = np.asarray(next_2weeks_dates)