
Python
Result Size: 722 x 999
prog.py Input + +
00
import random
import scipy.stats as stats
​
# Hypothesis Phase
hypothesis = "The coin is fair, with an equal chance of heads and tails."
​
# Experiment Phase
num_tosses = 2000
coin_tosses = [random.choice(["Heads", "Tails"]) for _ in range(num_tosses)]
​
# Data Collection Phase
num_heads = coin_tosses.count("Heads")
num_tails = coin_tosses.count("Tails")
​
# Analysis Phase
observed_proportion_heads = num_heads / num_tosses
expected_proportion_heads = 0.5  # In a fair coin toss, the expected proportion of heads is 0.5
​
# Perform a hypothesis test using a chi-squared test
chi_squared_stat = ((observed_proportion_heads - expected_proportion_heads) ** 2) / expected_proportion_heads
p_value = 1 - stats.chi2.cdf(chi_squared_stat, 1)
​
# Conclusion Phase
if p_value < 0.05:  # Using a significance level of 0.05
    conclusion = "The coin is biased."
else:
    conclusion = "The coin is fair."
​
print("\nHypothesis:", hypothesis)
print("Observed Proportion of Heads:", observed_proportion_heads)
print("Expected Proportion of Heads:", expected_proportion_heads)
print("Chi-Squared Statistic:", chi_squared_stat)
print("P-Value:", p_value)
print("Conclusion:", conclusion)
​
