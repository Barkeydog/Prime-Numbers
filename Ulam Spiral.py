import matplotlib.pyplot as plt

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def ulam_spiral(size):
    spiral, x, y, dx, dy, count = [[0] * size for _ in range(size)], size // 2, size // 2, 1, 0, 1

    for step in range(1, size, 2):
        for _ in range(step):
            if is_prime(count): spiral[x][y] = count
            count += 1
            x, y = x + dx, y + dy
        dx, dy = -dy, dx

    return spiral

def plot_ulam_spiral(spiral):
    plt.plot([num for row in spiral for num in row], marker='o', linestyle='None')
    plt.show()

size = 10001
plot_ulam_spiral(ulam_spiral(size))
