from sparkbadge import plot_normalizer as norm
from matplotlib import pyplot as plt

def points_to_string(data):
    i = 0
    x1 = []
    while i < len(data):
        x1.append(i)
        i += 1
    print("X1 = " + str(x1).strip('[]'))
    print("Y1 = " + str(data).strip('[]') + "\n")

    print("X2 = " + str(norm.normalize_x(len(data))).strip('[]'))
    print("Y2 = " + str(norm.normalize_y(data)).strip('[]') + "\n")

def points_to_plot(data):
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(data)
    ax1.set_title("Raw Plot")
    ax2.plot(norm.normalize_x(len(data)), norm.normalize_y(data, flip=True), 'tab:orange')
    ax2.set_title("Normalized Plot")
    fig.tight_layout(pad=1.0)
    fig.show()

y_sample = [0, 25, 5, 7, 9, 15, 16, 0]
points_to_string(y_sample)

# y_random = random.sample(range(0,50), 8)
# points_to_string(y_random)

print("M 0.0 0.0 L 21.43 20.0 L 42.86 4.0 L 64.29 5.6 L 85.71 7.2 L 107.14 12.0 L 128.57 12.8 L 150.0 0.0")
print(norm.sparkline_str(y_sample))

points_to_plot(y_sample)
