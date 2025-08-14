from itertools import product
from heapq import nlargest
import random

# Calculates dice probability naturally until it hits 9 or more dice
# then it switches to a Monte Carlo sim for approx calculations so
# your computer doesn't explode lmao
def calculate_top_two_probability(num_dice, target, sides = 6):
    if num_dice < 2:
        raise ValueError("Must roll at least 2 dice to calculate top two results")
    if target > 2 * sides:
        return 0.0, f"Maximum possible sum of two d{sides}s is {2 * sides}"
    if target <= 2:
        return 100.0, f"Minimum possible sum of two d{sides}s is 2"
    total_outcomes = sides ** num_dice
    successful_outcomes = 0
    max_exact_outcomes = 10_000_000
    if total_outcomes <= max_exact_outcomes:
        for roll in product(range(1, sides + 1), repeat=num_dice):
            if sum(nlargest(2, roll)) >= target:
                successful_outcomes += 1
        probability = (successful_outcomes / total_outcomes) * 100
    else:
        simulations = 100_000
        for _ in range(simulations):
            roll = [random.randint(1, sides) for _ in range(num_dice)]
            if sum(nlargest(2, roll)) >= target:
                successful_outcomes += 1
        probability = (successful_outcomes / simulations) * 100
    return probability, None
