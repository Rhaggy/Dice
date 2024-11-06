import matplotlib.pyplot as plot
import random

counts = [0]*16
for _ in range(1000):
    sum_dices = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    counts[sum_dices -3] += 1

print(counts)


values = range(3,19)

plot.bar(values, counts, edgecolor="maroon")
plot.xticks(values)
plot.xlabel("Sum dice")
plot.ylabel("Frequency")
plot.title("1000 rolles of two dices")
plot.show()