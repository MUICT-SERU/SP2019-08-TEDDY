def func(x, y):
    return np.array([
        x, y,
        2.7 + 0.5 * (np.sin(x) + np.cos(y)) -
        0.025 * (x**2 + y**2)
    ])

