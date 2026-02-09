# Euler's Identity Numerical Experiment
# This program demonstrates how truncation and rounding of π
# affect numerical computations, especially Euler’s identity:
# e^(iπ) + 1 = 0

import math
from decimal import Decimal, getcontext

# Set precision high enough
getcontext().prec = 110

# Pi to 110 decimal places
pi_str = str(Decimal(math.pi))

# Function to truncate and round pi at given decimal places
def truncate_pi(pi_str, decimals):
    truncated = pi_str[:pi_str.find('.') + decimals + 1]
    rounded = str(round(Decimal(pi_str), decimals))
    return truncated, rounded

# Other formula using pi: Euler's identity approximation
# For example, e^(i*pi) + 1 = 0, we approximate e^(i*pi) using truncated pi
import cmath

def euler_identity_approx(pi_val):
    return cmath.exp(1j * pi_val) + 1

# Baseline values
baseline_1 = Decimal('3.1415')
baseline_2 = Decimal('3.1416')

# Check truncation and rounding at 20th, 40th, 60th, 100th decimals
decimals_list = [20, 40, 60, 100]

print("Pi truncation and rounding differences:")
for d in decimals_list:
    trunc, round_val = truncate_pi(pi_str, d)
    print(f"At {d} decimals -> Truncated: {trunc}")
    print(f"At {d} decimals -> Rounded: {round_val}")
    print()

# Compare Euler identity results with the two baselines
print("Euler identity results using baselines:")
result_1 = euler_identity_approx(float(baseline_1))
result_2 = euler_identity_approx(float(baseline_2))
print(f"Using 3.1415: {result_1}")
print(f"Using 3.1416: {result_2}")
print(f"Difference: {abs(result_1 - result_2)}")
