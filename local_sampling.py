import numpy as np
import matplotlib.pyplot as plt

def generate_swarm(N):
    """Generates a swarm of N robots with random positions and random black/white colors."""
    positions = np.random.rand(N, 2)  # Positions in unit square [0, 1] x [0, 1]
    colors = np.random.choice(['black', 'white'], N)  # Randomly assign colors
    return positions, colors

def compute_distance(robot1, robot2):
    """Computes Euclidean distance between two robots."""
    return np.linalg.norm(robot1 - robot2)

def estimate_black_ratio(positions, colors, r):
    """Estimates the ratio of black robots using local sampling."""
    N = len(positions)
    estimated_ratios = []

    for i in range(N):
        distances = np.linalg.norm(positions - positions[i], axis=1)
        neighbors = (distances < r)
        black_count = np.sum((colors[neighbors] == 'black'))
        estimated_ratio = black_count / np.sum(neighbors)
        estimated_ratios.append(estimated_ratio)

    return np.mean(estimated_ratios)

def run_experiment(N, r, num_experiments):
    """Runs experiments for given swarm size N and sensor range r."""
    estimates = []
    for _ in range(num_experiments):
        positions, colors = generate_swarm(N)
        estimate = estimate_black_ratio(positions, colors, r)
        estimates.append(estimate * N)  # Convert ratio to number of black robots
    return np.mean(estimates), np.std(estimates)

def perform_all_experiments(swarm_sizes, sensor_ranges, num_experiments):
    """Runs the full set of experiments and collects results."""
    results = []
    for N in swarm_sizes:
        for r in sensor_ranges:
            mean_estimate, std_estimate = run_experiment(N, r, num_experiments)
            results.append((N, r, mean_estimate, std_estimate))
            print(f"Swarm Size: {N}, Sensor Range: {r}, Mean Estimate: {mean_estimate}, Std Dev: {std_estimate}")
    return results

def plot_results(results):
    """Plots the mean and standard deviation of the estimates."""
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))

    swarm_sizes = sorted(set([res[0] for res in results]))
    sensor_ranges = sorted(set([res[1] for res in results]))

    for r in sensor_ranges:
        means = [res[2] for res in results if res[1] == r]
        std_devs = [res[3] for res in results if res[1] == r]
        axs[0].plot(swarm_sizes, means, label=f'Sensor Range: {r}')
        axs[1].plot(swarm_sizes, std_devs, label=f'Sensor Range: {r}')

    axs[0].set_xlabel('Swarm Size')
    axs[0].set_ylabel('Mean Estimate of Black Robots')
    axs[0].set_title('Mean Estimate of Black Robots vs. Swarm Size')
    axs[0].legend()

    axs[1].set_xlabel('Swarm Size')
    axs[1].set_ylabel('Standard Deviation')
    axs[1].set_title('Standard Deviation of Estimates vs. Swarm Size')
    axs[1].legend()

    plt.tight_layout()
    plt.savefig("task5.2_results_plot.png")
    plt.show()

if __name__ == "__main__":
    swarm_sizes = np.arange(2, 201)
    sensor_ranges = np.linspace(0.02, 0.5, 10)
    num_experiments = 1000

    print("Running experiments for Task 5.2 Local Sampling in a Swarm")
    results = perform_all_experiments(swarm_sizes, sensor_ranges, num_experiments)
    
    print("\nPlotting results")
    plot_results(results)
