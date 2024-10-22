import matplotlib.pyplot as plt
with open("data (1).txt", "r") as f:
    t = [int(i) for i in f.read().split("\n")]
    y = [i*3.3/256 for i in t]
with open("settings (1).txt", "r") as f1:
    t1 = [float(i) for i in f1.read().split("\n")]
    x = [t1[1]*j for j in range(len(t))]
print(x)
print(y)
x1 = []
y1 = []
for i in range(len(t)):
    if (i % 20 == 0):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(dpi=200)
#err_line = plt.errorbar(x, y, xerr=0.0001, yerr=0.0001, fmt='b', marker=".")
plt.plot(x1, y1, label="Зарядка-разрядка конденсатора", linestyle='-', marker="o", color='blue',
          linewidth=1,
          ms=6)
plt.minorticks_on()
plt.grid(which="major", color="black", linewidth = 0.5)
plt.grid(which="minor", color="black", ls="-", linewidth=0.05)

plt.text(1, 0.5, "зарядка")
plt.text(6, 2, "разрядка")

plt.ylabel("Напряжение, В")
plt.xlabel("Время, сек.")

plt.title("График зависимости напряжения на конденсаторе от времени.")

plt.legend(loc=8)

plt.savefig("test.png")

plt.show()