#!/usr/bin/env python
# coding: utf-8

# Here’s a Python script that can calculate the probability and odds of winning a prize greater than the break-even amount, based on the inputs discussed. The script allows you to input the total number of tickets, odds of winning, percentage of break-even prizes, and the number of tickets you plan to buy. The output provides the probability and odds of winning a prize greater than the break-even amount.

# In[ ]:


#scratchMath

import math

def calculate_probabilities(total_tickets, odds_of_winning, percentage_break_even, tickets_to_buy):
    # Calculate the probability of winning any prize
    prob_of_winning_any = 1 / odds_of_winning

    # Calculate the probability of winning a break-even prize
    prob_of_break_even = prob_of_winning_any * (percentage_break_even / 100)

    # Calculate the probability of winning more than break-even
    prob_of_greater_than_break_even = prob_of_winning_any - prob_of_break_even

    # Calculate the probability of losing on all tickets
    prob_of_losing = 1 - prob_of_greater_than_break_even
    prob_of_losing_all = prob_of_losing ** tickets_to_buy

    # Calculate the probability of winning at least once (more than break-even)
    prob_of_winning_at_least_once = 1 - prob_of_losing_all

    # Calculate the odds of winning more than break-even
    odds_of_winning_greater_than_break_even = 1 / prob_of_greater_than_break_even

    # Print results
    print(f"Probability of winning any prize: {prob_of_winning_any:.4f}")
    print(f"Probability of winning break-even prize: {prob_of_break_even:.4f}")
    print(f"Probability of winning more than break-even prize: {prob_of_greater_than_break_even:.4f}")
    print(f"Probability of losing on all {tickets_to_buy} tickets: {prob_of_losing_all:.4f}")
    print(f"Probability of winning at least one prize greater than break-even: {prob_of_winning_at_least_once:.4f}")
    print(f"Odds of winning more than break-even prize: 1 in {odds_of_winning_greater_than_break_even:.2f}")

# Example usage
total_tickets = 44  # Total remaining tickets
odds_of_winning = 4.79  # Odds of winning any prize (including break-even)
percentage_break_even = 75  # Percentage of winning tickets that are break-even prizes
tickets_to_buy = 5  # Number of tickets you plan to buy

calculate_probabilities(total_tickets, odds_of_winning, percentage_break_even, tickets_to_buy)


# 

# Explanation:
# total_tickets: The total number of tickets remaining.
# odds_of_winning: The odds of winning any prize, including break-even prizes.
# percentage_break_even: The percentage of winning tickets that are break-even prizes.
# tickets_to_buy: The number of tickets you plan to purchase.

# Outputs:
# Probability of winning any prize: The probability of winning any prize, including break-even.
# Probability of winning a break-even prize: The probability of winning just the break-even prize.
# Probability of winning more than break-even: The probability of winning a prize greater than the break-even amount.
# Probability of losing on all tickets: The probability that all the tickets you buy will be losers.
# Probability of winning at least one prize greater than break-even: The probability of winning at least one prize greater than break-even among the tickets you buy.
# Odds of winning more than break-even: The odds of winning a prize greater than break-even.

# Customizing the Script:
# Adjust the total_tickets and tickets_to_buy variables depending on your scenario.
# Modify the percentage_break_even to reflect a different distribution of break-even prizes if you have more accurate data.
# This script will help you assess your chances and find the best scenarios to maximize your potential winnings while understanding the risks involved.
