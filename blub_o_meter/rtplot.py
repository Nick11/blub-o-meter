import LSM6DS3
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

sensor = LSM6DS3.LSM6DS3()
n_drops = 10
npoints = n_drops
# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, npoints), ax.set_xticks([])
ax.set_ylim(0, 300), ax.set_yticks([])

# Create rain data
data = np.zeros([n_drops, 2])

# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(data[:, 0], data[:, 1])

global mean
global n
mean = np.zeros([1, 2])
n = 0

def update(i):
    newdata = np.array([[sensor.readRawAccelY(), sensor.readRawAccelZ()]])
    global mean
    global n
    mean = (n * mean + newdata) / (n + 1)
    n = n + 1
    if i < npoints:
        data[i, :] = newdata
    else:
        temp = data[1:npoints, :]
        data[0:npoints-1, :] = temp
        data[npoints-1, :] = newdata

    corr_data = data - np.tile(mean, (npoints, 1))
    corr_data_norm = np.linalg.norm(corr_data, ord=2, axis=1)
    corr_data_with_time = np.column_stack((range(0, npoints), corr_data_norm))
    print(corr_data_with_time)
    scat.set_offsets(corr_data_with_time)

ani = anim.FuncAnimation(fig, update, interval=100)

plt.show()
