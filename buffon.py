import numpy as np 
import matplotlib.pyplot as plt 

def simulate_buffon_needle(n, b=0.7, s=1):

    """
    Simulate Buffon's needle experiment for n trials.
    Args:
    - n (int): Number of trials.
    - b (float): Length of the needle
    - s (float): Distance between the lines

    Returns:
    - (float): Probability of intersection.
    """

    #Ramdom distance from the middle of the line to the nearest line
    #Random angles of the needle with the verticle
    distances = np.random.uniform(0, s/2, n)
    angles = np.random.uniform(0, np.pi/2, n)

    #Check for intersection
    intersections = distances <= (b / 2) * np.sin(angles)

    #Calculate probability
    P = np.mean(intersections) 

    return P


def estimate_pi(P, b=0.7, s=1):
    """
    Estimate the value of pi using Buffon's needle formula
    Args:
    - P (float): Probability of intersection.
    - b (float): Length of the needle.
    - s (float): Distance between the lines.

    Returns:
    - Pi (float): Estimated value of pi.
    """

    Pi = 2 * b (s * P)
    return Pi

def experiment_and_plot():
    #Number of trials
    trial_counts = np.arange(10, 1001, 10) #Return evenly spaced values within a given interval.

    #Nubmer of experiments
    num_experiments = 10000

    #Store std_dev of intersection probabilities
    std_devs = []

    for n in trial_counts:
        probabilities = [simulate_buffon_needle(n) for _ in range(num_experiments)]
        std_dev = np.std(probabilities)
        std_devs.append(std_dev)

    #Plot std_dev over number of trials
    plt.plot(trial_counts, std_devs)
    plt.xlabel('Number of Trials')
    plt.ylabel('Standard Deviation of Intersection Probabilities')
    plt.title('Task 5.1_b) Standard Deviation of Intersection Probabiliteis vs. Number of Trials')
    plt.savefig("task5.1b_plot.png")
    plt.show()

    print(f"Standard deviations over trials: {std_devs}")

    
def confidence_intervals():
    #Number of trials
    max_n = 100
    trial_counts = np.arange(1, max_n + 1)
    num_experiments = 10000

    #Store measured probabilities and their confidence intervals
    measured_probs = []
    lower_bounds = []
    upper_bounds = []

    for n in trial_counts:
        probabilities = [simulate_buffon_needle(n) for _ in range(num_experiments)]
        mean_prob = np.mean(probabilities)
        measured_probs.append(mean_prob)

        #Calculate 95% confidence interval for a binomal proportion
        #The value of z* for a confidence level of 95% is 1.96.
        ci_low = mean_prob - 1.96 * np.sqrt((mean_prob * (1-mean_prob)) / n)
        ci_high = mean_prob + 1.96 * np.sqrt((mean_prob * (1-mean_prob)) / n)
        lower_bounds.append(ci_low)
        upper_bounds.append(ci_high)

    #Plot measured probability and confidence intervals
    plt.plot(trial_counts, measured_probs, label='Measured Probability')
    plt.fill_between(trial_counts, lower_bounds, upper_bounds, color='b', alpha=0.2, label='95% CI')
    plt.xlabel('Number of Trials')
    plt.ylabel('Measured Probability')
    plt.title('Task 5.1_c)Measured Probability and 95% Confidence Interval')
    plt.legend
    plt.savefig("task5.1c_plot.png")
    plt.show

    # Print measured probabilities for inspection
    print(f"Measured probabilities: {measured_probs}")
    print(f"95% confidence intervals: lower_bounds={lower_bounds}, upper_bounds={upper_bounds}")



def outside_confidence_ratio():
    #Number of trials
    max_n = 100
    trial_counts = np.arange(1, max_n + 1)
    num_experiments = 100
   
   
    # Store the ratio of experiments outside the 95% confidence interval
    outside_ratios = []

    #P= 2 * b / (s * pi)
    true_prob = 2 * 0.7 / (1 * np.pi)

    for n in trial_counts:
        outside_count = 0
        for _ in range(num_experiments):
            probabilities = [simulate_buffon_needle(n) for _ in range(num_experiments)]
            mean_prob = np.mean(probabilities)
            ci_low = mean_prob - 1.96 * np.sqrt((mean_prob * (1-mean_prob)) / n)
            ci_high = mean_prob + 1.96 * np.sqrt((mean_prob * (1-mean_prob)) / n)

            if true_prob < ci_low or true_prob > ci_high:
                outside_count += 1
        outside_ratios.append(outside_count / num_experiments)

    # Plot the ratio of experiments outside the 95% confidence interval
    plt.plot(trial_counts, outside_ratios)
    plt.xlabel('Number of Trials')
    plt.ylabel('Ratio Outside 95% Confidence Interval')
    plt.title('Task 5.1_d) Ratio of Experiments Outside 95% Confidence Interval')
    plt.savefig("task5.1d_plot.png")
    plt.show()

    # Print the ratios for inspection
    print(f"Ratios outside 95% confidence interval: {outside_ratios}")


if __name__ == "__main__":

    print("Running task 5.1b: Standard Deviation of Intersection Probabilities")
    #experiment_and_plot()
    
    print("\nRunning task 5.1c: Measured Probability and 95% Confidence Interval")
    #confidence_intervals()
    
    print("\nRunning task 5.1d: Ratio of Experiments Outside 95% Confidence Interval")
    outside_confidence_ratio()


    

        
