import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from math import sqrt, log

ys = [30]
xs = range(0, 501)
np.random.seed(seed=42)
for delta in np.random.normal(0, 0.5, 500):
    ys.append(ys[-1] + delta)

plt.plot(ys)
plt.ylabel('Stock Price ($)')
plt.xlabel('Elapsed Time (min)')
# plt.savefig('1.01.svg')
# plt.show()
r = stats.linregress(xs, ys)
line = [r.slope * x + r.intercept for x in xs]

error = [y - y0 for y, y0 in zip(ys, line)]
std = np.std(error)
top = [y + std for y in line]
bottom = [y - std for y in line]
plt.plot(xs, ys)
plt.plot(xs, line)
plt.plot(xs, top)
plt.plot(xs, bottom)
plt.ylabel('Stock Price ($)')
# plt.show()
