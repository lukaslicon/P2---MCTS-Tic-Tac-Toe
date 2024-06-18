# Ultimate Tic-Tac-Toe with Monte Carlo Tree Search (MCTS) Bot

## Introduction
This project involves creating a bot that plays Ultimate Tic-Tac-Toe using Monte Carlo Tree Search (MCTS) in Python. Ultimate Tic-Tac-Toe is an advanced version of the classic Tic-Tac-Toe game where players play on a grid of 9 smaller Tic-Tac-Toe boards to complete a giant row, column, or diagonal. The MCTS bot will be evaluated through various experiments to ensure its effectiveness and performance.

## Project Structure
The project includes the following files and directories:

- `p2_sim.py`: Simulator for running multiple games between pairs of bots.
- `p2_play.py`: Interactive version of the game for human and bot players.
- `mcts_vanilla.py`: Implementation of the MCTS bot with a full, random rollout strategy.
- `mcts_modified.py`: Modified MCTS bot with heuristic rollout strategy and potential other enhancements.
- `mcts_node.py`: Class for constructing the game tree nodes used in MCTS.
- `random_bot.py`: Bot that selects a random action every turn.
- `rollout_bot.py`: Bot that performs rollouts to decide the best move.

## Running the Game
To run the game interactively:
```sh
$ python p2_play.py PLAYER1 PLAYER2
# Example:
$ python p2_play.py human mcts_vanilla
```
To run a simulation between two bots:
```sh
$ python p2_sim.py PLAYER1 PLAYER2
# Example:
$ python p2_sim.py mcts_vanilla random_bot
```

## MCTS Bot Implementation
Your MCTS bot should implement the following functions in both `mcts_vanilla.py` and `mcts_modified.py`:

- `think(board, state)`: Main function to decide the best move.
- `traverse_nodes(node, board, state)`: Selection phase - navigate the tree.
- `expand_leaf(node, board, state)`: Expansion phase - add a new node.
- `rollout(board, state)`: Simulation phase - play out the game randomly or heuristically.
- `backpropagate(node, result)`: Backpropagation phase - update nodes with results.

### MCTSNode Class
The `MCTSNode` class contains the following attributes:
- `parent`: Parent node.
- `parent_action`: Action taken to transition from the parent to the current node.
- `child_nodes`: Dictionary mapping an action to a child node.
- `untried_actions`: List of actions not yet tried.
- `wins`: Number of wins from this node onwards.
- `visits`: Number of times this node was visited.
- `tree_to_string(horizon)`: Returns a string representation of the game tree up to a specified depth.

## Requirements
1. Implement `mcts_vanilla.py` to use MCTS with a full, random rollout strategy.
2. Implement `mcts_modified.py` with a heuristic rollout strategy and possibly other enhancements.
3. Perform two experiments and analyze the results:
    - **Experiment 1 - Tree Size**: Test different tree sizes for MCTS and analyze the results.
    - **Experiment 2 - Heuristic Improvement**: Compare the performance of the modified MCTS bot against the vanilla version.
4. (Optional) **Experiment 3 - Time Constraint**: Test the MCTS bots with a fixed time budget instead of a fixed tree size.

## Experiments
### Experiment 1 - Tree Size
Pit two versions of the vanilla MCTS bot against each other with different tree sizes. Test at least four sizes for Player 2 against a fixed size of 100 nodes for Player 1 over 100 games each. Plot and analyze the results.

### Experiment 2 - Heuristic Improvement
Compare the performance of the modified MCTS bot against the vanilla version with equal tree sizes (suggested size: 1000). Conduct 3 sets of 100 games with different tree sizes and analyze the results.

### Experiment 3 - Time Constraint (Optional)
Test the bots with a time budget of 1 second and analyze the difference in tree size and performance between the vanilla and modified versions.

## Submission Instructions
Submit a zip file named `Lastname-Firstname.zip` containing:
- A README.md (this file) naming the teammates and explaining the modifications done for `mcts_modified.py`.
- `mcts_vanilla.py` implementing the MCTS functions.
- `mcts_modified.py` implementing the MCTS functions with heuristic rollout strategy.
- `experiment1.pdf` with the analysis of Experiment 1 results.
- `experiment2.pdf` with the analysis of Experiment 2 results.

## References
For more information on MCTS, refer to the survey paper: [A Survey of Monte Carlo Tree Search Methods](http://diego-perez.net/papers/MCTSSurvey.pdf).

Happy coding and good luck!
