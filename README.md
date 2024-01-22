# P2_MCTS-Tic-Tac-Toe
In this programming assignment you will need to implement, in Python, a bot that plays Ultimate Tic-
Tac-Toe using Monte Carlo Tree Search (MCTS). Ultimate Tic-Tac-Toe is a turn-based two-player
game where players have to play a grid of 9 tic-tac-toe games simultaneously in order to complete
one giant row, column, or diagonal. The catch is that each on each player’s turn, they can only place
a cross or circle in one square of one board; and whichever square they pick, their opponent must
play on the corresponding (possibly different) board. The bots will be implemented using a digital
version of this game implemented in python, which is described in detail in the next sections. In order
to evaluate your implementation, you will also need to perform and analyze two different
experiments.

In order to run the game interactively you need to execute the following command (assuming you
are in the /src folder):
- $ python p2_play.py human human
- python p2_play.py PLAYER1 PLAYER2, where either can be ‘human’,

The game can also be executed in a simulation mode, where there is no rendering. This is useful to
test how one bot plays against another. To execute this type of simulation, you can run the following
command:
- $ python p2_sim.py PLAYER1 PLAYER2
- python p2_sim.py PLAYER1 PLAYER2
‘mcts_vanilla’, ‘mcts_modified’, ‘random_bot’, ‘rollout_bot’.

When you run this code you should see a textual display of the board and a prompt for which board
and which square to move in.