# CRS04 Exercise

## Team Members
- **Minsol Kim**
- **BhargavSolanki**

## Overview
This repository hosts our group's submission for Task Sheet 4 of Collective robotics and scalability.



## Task 5.1: Buffon's Needle

### Description
Buffon's Needle problem is a classic probability puzzle that involves dropping a needle of length `b` onto a plane ruled with parallel lines spaced `s` apart. 
The goal is to determine the probability `P` that the needle will intersect one of the lines and use this probability to approximate π.

### Implementation
- **Simulation**: The simulation involves dropping a needle on a single line segment of width `s` and checking if it intersects based on the needle’s angle and distance from the center to the nearest line.
- **Intersection Probability**: The intersection probability `P` is calculated and used to estimate π according to the formula:
  \[
  \pi \approx \frac{2b}{sP}
  \]

### What We Encountered
**Problem**: In Task 5.1.d, the ratio of experiments for which the true probability was outside the 95% confidence interval was always 0. This suggests that the estimated probabilities always fell within the expected range, which is statistically unlikely.

#### Potential Reasons:
1. **Statistical Anomalies**: Given the random nature of the experiments, it's possible that the simulation results are showing a rare scenario where the estimates are unusually accurate. However, this should not consistently result in a ratio of 0 over many trials.

3. **Confidence Interval Calculation**: There may be a bug or incorrect implementation in the calculation of the 95% confidence intervals. The intervals may be too wide, consistently covering the true probability.


### Code Explanation
- simulate_buffon_needle(n, b, s): Simulates n needle drops, returning the intersection probability.
- estimate_pi(P, b, s): Estimates π using the intersection probability.
- experiment_and_plot(): Conducts experiments and plots the standard deviation.
- confidence_intervals(): Computes and plots the confidence intervals.
- outside_confidence_ratio(): Measures and plots the ratio of experiments outside the confidence interval.


### What we failed
At Task 5.1.d, confidence ratio outside of 95% is always 0. However, assuming from overall possibilities, it can't be 0.
