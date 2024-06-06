import numpy as np
import matplotlib.pyplot as plt

# Function to generate positions and colors of robots in the swarm
def create_swarm(num_robots):
    positions = np.random.rand(num_robots, 2)  # robots with positions (x, y) in [0, 1] x [0, 1]
    colors = np.random.choice(['black', 'white'], num_robots)  # Each robot is black or white with equal probability
    return positions, colors

# Function to calculate Euclidean distance between two points
def compute_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Function to estimate the number of black robots from a local sample
def black_robots_estimation(positions, colors, sensor_range):
    N = len(positions)
    estimates = []
    for i in range(N):
        neighbors = [j for j in range(N) if compute_distance(positions[i], positions[j]) < sensor_range]
        black_count = sum(1 for j in neighbors if colors[j] == 'black')
        estimates.append(black_count / len(neighbors) * N if neighbors else 0)
    return np.mean(estimates)

# Simulation Parameters
swarm_sizes = range(2, 201)
r_values = np.linspace(0.02, 0.5, 25)
num_experiments = 5

# Store results
mean_estimates = np.zeros((len(swarm_sizes), len(r_values)))
std_estimates = np.zeros((len(swarm_sizes), len(r_values)))

# Run the simulations
for i, N in enumerate(swarm_sizes):
    for j, r in enumerate(r_values):
        estimates = []
        for _ in range(num_experiments):
            positions, colors = create_swarm(N)
            estimate = black_robots_estimation(positions, colors, r)
            estimates.append(estimate)
        mean_estimates[i, j] = np.mean(estimates)
        std_estimates[i, j] = np.std(estimates)


# Plotting results
plt.figure(figsize=(14, 6))

# Plot mean estimates
plt.subplot(1, 2, 1)
for j, r in enumerate([0.1, 0.2, 0.3, 0.4, 0.5]):
    plt.plot(swarm_sizes, mean_estimates[:, j * 5], label=f'r={r}')
plt.xlabel('Swarm Size N')
plt.ylabel('Mean Estimate of Black Robots')
plt.legend()
plt.title('Mean Estimates for Different Sensor Ranges')

# Plot standard deviation
plt.subplot(1, 2, 2)
for j, r in enumerate([0.1, 0.2, 0.3, 0.4, 0.5]):
    plt.plot(swarm_sizes, std_estimates[:, j * 5], label=f'r={r}')
plt.xlabel('Swarm Size N')
plt.ylabel('Standard Deviation of Estimate')
plt.legend()
plt.title('Standard Deviation for Different Sensor Ranges')

plt.tight_layout()
plt.show()
