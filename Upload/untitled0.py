# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:05:01 2020

@author: MAYANK SHAW
"""

import numpy  as np
from iterative_policy_evaluation import print_values, print_policy
from grid_world import standard_grid, negative_grid

SMALL_ENOUGH = 10e-4
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

def play_game(grid, policy):
    # returns a list of states and corresponding returns
    # reset game to start at random position
    #we need to do this because given our current deterministic policy
    # we would never end up at certain states, but we stil want to measure them
    start_states = grid.actions.keys()
    start_idx = np.random.choice(len(start_states))
    grid.set_state(start_states[start_idx])
    
    s = grid.current_state()
    states_and_rewards = [(s, 0)]  #list of tuples of state and rewards
    while not grid.game_over():
        a = policy[s]
        r = grid.move(a)
        s = grid.current_state()
        states_and_rewards.append((s,r))
    # calculate the returns by working backwards from terminal state    
    G = 0
    states_and_returns = []
    first = True
    for s, r in reversed(states_and_rewards):
        # the value of terminal state is 0 by definition
        # we should ignore the first state we encounter
        if first:
            first = False
        else:
            states_and_returns.append((s, G))
        G = r + GAMMA*G
    states_and_returns.reverse()  # we want it to be in order of states we visited
    return states_and_returns
    
if __name__=='__main__':
    # use standard grid again (0 for every step) so that we can compare
    # to iterative policy evaluation
    
    grid = standard_grid()
    # print rewards
    print('Rewards: ')
    print_values(grid.rewards, grid)
    
    # state -> action
    policy = {
        (2, 0): 'U',
        (1, 0): 'R',
        (0, 0): 'R',
        (0, 1): 'R',
        (0, 2): 'R',
        (1, 2): 'R',
        (2, 1): 'R',
        (2, 2): 'R',
        (2, 3): 'U',        
    }
    
    #initialize V(s) and returns
    V = {}
    returns = {} # dictionary of state->list of returns we have received
    states = grid.all_states()
    for s in states:
        if s in grid.actions:
            returns[s] = []
        else:
            # terminal state or state we cant otherwise go to
            V[s] = 0
    
    #repeat
    for t in range(100):
        
        # generate an episode using pi
        states_and_returns = play_game(grid, policy)
        seen_states = set()
        for s, G in states_and_returns:
            # check if we have already seen s
            # called first visit mc policy evaluation
            if s not in seen_states:
                returns[s].append(G)
                V[s] = np.mean(returns[s])
                seen_states.add(s)
        
    print('Values: ')
    print_values(V, grid)
    print('Policy: ')
    print_policy(policy, grid)