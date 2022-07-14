from matplotlib import markers
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(
        rw.x_values, rw.y_values,
        color='m', linewidth=1, markersize=1
    )

    # Emphasize the first and last points.
    plt.plot(0, 0, color='green', markersize=100)
    plt.plot(
        rw.x_values[-1], rw.y_values[-1],
        color='red', markersize=100
    )

    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another molecular  motion? (y/n): ")
    if keep_running == 'n':
        break