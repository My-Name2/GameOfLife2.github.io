import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the grid
def random_grid(N):
    """Returns a grid of NxN random values"""
    return np.random.choice([0, 1], N*N, p=[0.7, 0.3]).reshape(N, N)

def update(frameNum, img, grid, N):
    """Updates the grid according to Conway's rules"""
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Get the number of live neighbors
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))

            # Apply Conway's rules
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    # Update the image data
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Main function
def main():
    N = 50  # Grid size
    update_interval = 200  # Update interval in milliseconds

    grid = random_grid(N)

    # Set up the figure and axis
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    # Start the animation
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10, interval=update_interval, save_count=50)

    plt.show()

if __name__ == '__main__':
    main()
