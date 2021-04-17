import random

def sparkline_str(data):
    xpoints = normalize_x(len(data))
    ypoints = normalize_y(data)

    xpoints[0] += -1
    xpoints[len(xpoints)-1] += 1

    pathstr = "M"
    i = 0
    while i < len(data):
        if i == (len(data) - 1):
            pathstr += " " + str(xpoints[i]) + " " + str(ypoints[i])
            break
        else:
            pathstr += " " + str(xpoints[i]) + " " + str(ypoints[i]) + " L"
            i += 1
            continue
    return pathstr

def normalize_x(n, plot_width=150):
    i = 0
    x_scale = plot_width / (n - 1)
    x_points = []
    while i < n:
        t = i * x_scale
        x_points.append(round(t, 2))
        i += 1
    return x_points

def normalize_y(raw_data, plot_height=20):
    i = 0
    y_max = max(raw_data)
    y_scale = plot_height / y_max
    y_points = []
    for p in raw_data:
        t = (raw_data[i] * y_scale)
        y_points.append(round(t, 2))
        i += 1
    return y_points





