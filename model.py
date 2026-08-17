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

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

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

