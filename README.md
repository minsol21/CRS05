# CRS04 Exercise

## Team Members
- **Minsol Kim**
- **BhargavSolanki**

## Overview
This repository hosts our group's submission for Task Sheet 4 of Collective robotics and scalability.



## Task 5.1: Buffon's Needle
file name: buffon.py

### Description
Buffon's Needle problem is a classic probability puzzle that involves dropping a needle of length `b` onto a plane ruled with parallel lines spaced `s` apart. 
The goal is to determine the probability `P` that the needle will intersect one of the lines and use this probability to approximate π.

### Implementation
- **Simulation**: The simulation involves dropping a needle on a single line segment of width `s` and checking if it intersects based on the needle’s angle and distance from the center to the nearest line.
- **Intersection Probability**: The intersection probability `P` is calculated and used to estimate π according to the formula:
  \[
  \pi \approx \frac{2b}{sP}
  \]

### Code Explanation
- **`simulate_buffon_needle(n, b, s)`**: Simulates n needle drops, returning the intersection probability.
- **`estimate_pi(P, b, s)`**: Estimates π using the intersection probability.
- **`experiment_and_plot()`**: Conducts experiments and plots the standard deviation.
- **`confidence_intervals()`**: Computes and plots the confidence intervals.
- **`outside_confidence_ratio()`**: Measures and plots the ratio of experiments outside the confidence interval.


### What We Encountered
**Problem**: In Task 5.1.d, the ratio of experiments for which the true probability was outside the 95% confidence interval was always 0. This suggests that the estimated probabilities always fell within the expected range, which is statistically unlikely. 
Also, we reduced the number of experiments from 10000 to 100 since running the code was too slow.

#### Potential Reasons:
1. Given the random nature of the experiments, it's possible that the simulation results are showing a rare scenario where the estimates are unusually accurate. However, this should not consistently result in a ratio of 0 over many trials.

3. There may be a bug or incorrect implementation in the calculation of the 95% confidence intervals. The intervals may be too wide, consistently covering the true probability.


## Task 5.2: Local Sampling in a Swarm
file name: 
This task involves simulating a swarm of robots uniformly distributed over a unit square. Each robot is randomly assigned a color, either black or white, with equal probability. The goal is for each robot to estimate the overall number of black robots in the swarm based on local observations of its neighborhood, defined by a sensor range `r`.


### Simulation Process
1. **Swarm Generation**: Robots are distributed randomly within the unit square, each assigned a color (black or white) with a 50% chance.
2. **Local Sampling**: Each robot perceives the color of all robots within its sensor range `r`. This includes itself and all other robots whose distance from it is less than `r`.
3. **Estimate Calculation**: Based on the local ratio of black robots, each robot estimates the overall ratio of black robots in the swarm.

### Code Explanation
1. **`generate_swarm(N)`**: This function generates `N` robots, each with a random position in the unit square and a random color (black or white).


2. **`compute_distance(robot1, robot2)`**: Computes the Euclidean distance between two robots.


3. **`estimate_black_ratio(positions, colors, r)`**: Estimates the ratio of black robots within each robot's sensor range.
   
    
4. **`run_experiment(N, r, num_experiments)`**: Runs multiple experiments for given swarm size and sensor range, returning mean and standard deviation.
   
    
5. **`perform_all_experiments(swarm_sizes, sensor_ranges, num_experiments)`**: Collects results for different configurations and plots them.
 
    
### Plotting
- **`plot_results(results)`**: Creates and saves plots for mean and standard deviation of estimates.
   
