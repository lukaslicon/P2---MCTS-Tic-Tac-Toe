from mcts_node import MCTSNode
from p2_t3 import Board
from random import choice
from math import sqrt, log

num_nodes = 1000
explore_factor = 1.0

def traverse_nodes(node, board, state, bot_identity):
    while not board.is_ended(state) and not node.untried_actions and node.child_nodes:
        if node.untried_actions:
            return expand_leaf(node, board, state)
        else:
            action = max(node.child_nodes, key=lambda a: ucb(node.child_nodes[a], False))
            node = node.child_nodes[action]
            state = board.next_state(state, action)

    return node, state

def expand_leaf(node, board, state):
    if not node.untried_actions:
        return node, state

    action = choice(node.untried_actions)
    node.untried_actions.remove(action)

    new_node = MCTSNode(parent=node, parent_action=action, action_list=board.legal_actions(state))
    node.child_nodes[action] = new_node
    state = board.next_state(state, action)

    return new_node, state

def rollout(board, state):
    while not board.is_ended(state):
        action = choice(board.legal_actions(state))
        state = board.next_state(state, action)
    return state

def backpropagate(node, won):
    while node is not None:
        node.visits += 1
        if won:
            node.wins += 1
        node = node.parent

def ucb(node, is_opponent):
    if node.visits == 0:
        return float('inf')

    exploitation = node.wins / node.visits
    exploration = explore_factor * sqrt(log(node.parent.visits) / node.visits)

    return exploitation + exploration if not is_opponent else 1 - exploitation + exploration

def get_best_action(root_node):
    if not root_node.child_nodes:
        return None

    return max(root_node.child_nodes, key=lambda a: root_node.child_nodes[a].visits)

def is_win(board, state, identity_of_bot):
    outcome = board.points_values(state)
    assert outcome is not None, "is_win was called on a non-terminal state"
    return outcome[identity_of_bot] == 1

def think(board, current_state):
    bot_identity = board.current_player(current_state)
    root_node = MCTSNode(parent=None, parent_action=None, action_list=board.legal_actions(current_state))

    for _ in range(num_nodes):
        state = current_state
        node = root_node

        node, state = traverse_nodes(node, board, state, bot_identity)
        node, state = expand_leaf(node, board, state)
        rollout_state = rollout(board, state)
        backpropagate(node, is_win(board, rollout_state, bot_identity))

    best_action = get_best_action(root_node)
    print(f"Action chosen: {best_action}")
    return best_action
