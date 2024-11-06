import matplotlib.pyplot as plot
import random

counts = [0]*11
for _ in range(1000):
    sum_dices = random.randint(1,6) + random.randint(1,6)
    counts[sum_dices -2] += 1

print(counts)


values = [2,3,4,5,6,7,8,9,10,11,12]

plot.bar(values, counts, color = "green", edgecolor="maroon")
plot.xticks(values)
plot.xlabel("Sum dice")
plot.ylabel("Frequency")
plot.title("1000 rolles of two dices")
plot.show()