"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    values = np.asarray(values)
    probabilities = np.asarray(probabilities)
    return float(np.sum(values*probabilities))
    pass

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    faces = np.arange(1, sides + 1)
    probs = np.full(sides, 1.0 / sides)
    
    # Calculate expected value of a single roll (mu)
    mu = expected_value(faces, probs)
    
    # Calculate optimal payout for each face
    payouts = np.maximum(faces, mu)
    total_val = expected_value(payouts, probs)
    
    # Reroll only when first roll face is strictly less than mu
    reroll_faces = [int(f) for f in faces if f < mu]
    
    return {
        'value': total_val,
        'reroll_faces': reroll_faces
    }
    pass

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    best_value = -float('inf')
    best_threshold = 1
    for t in range(1 , sides+1):
        keep_avg = (t + sides)/ 2.0
        cost_term = ((t - 1)/(sides - t + 1)) * reroll_cost
        v_t = keep_avg - cost_term
        if v_t > best_value:
         best_value = v_t
         best_threshold = t
    return {'threshold':best_threshold,'value':best_value}
    pass

# Step 4 - red_black_card_game_value
from functools import lru_cache
def red_black_card_game_value(num_red, num_black):
    @lru_cache(maxsize=None)
    def V(r: int, b: int) -> float:
        if r == 0: 
            return 0.0
        if b == 0: 
            return float(r)
        return max(0.0, (r * (1 + V(r - 1, b)) + b * (-1 + V(r, b - 1))) / (r + b))

    if num_red == 0 or num_black == 0:
        cont = float(num_red) if num_black == 0 else -1.0
    else:
        cont = (num_red * (1 + V(num_red - 1, num_black)) + num_black * (-1 + V(num_red, num_black - 1))) / (num_red + num_black)

    return {'value': max(0.0, cont), 'stop_now': cont <= 0.0}

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    bid = fair_value - spread_width/2
    ask = fair_value + spread_width/2
    return {'bid':bid,'ask':ask}
    pass

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

