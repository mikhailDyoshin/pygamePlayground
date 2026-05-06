import matplotlib.pyplot as plt

from common.utils import get_data_from_file

data = get_data_from_file("data.txt")

population, speed, vision = data
timestamps = list(range(len(population)))


plt.figure(figsize=(3, 9))

plt.subplot(311)
plt.plot(timestamps, population)
plt.subplot(312)
plt.plot(timestamps, speed)
plt.subplot(313)
plt.plot(timestamps, vision)
plt.suptitle("Evolution")
plt.savefig("evolution.png")
