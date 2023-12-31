# Define the tree with modified node values
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [10, 12],
    'E': [8, 6],
    'F': [4, 6],
    'G': [14, 11],
}

# Define the minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(node, alpha, beta, is_maximizing):
    # Check if the node is a string, indicating a non-terminal node
    if isinstance(node, str):
        # Get the children of the current node
        children = tree[node]
        
        # If it's a maximizing node
        if is_maximizing:
            value = -float('inf')
            # Iterate through the children
            for child in children:
                # Recursively call the function for the child node (switch to minimizing)
                value = max(value, minimax_alpha_beta(child, alpha, beta, False))
                # Update alpha with the maximum value
                alpha = max(alpha, value)
                # Prune the tree if necessary (alpha >= beta)
                if alpha >= beta:
                    break
            return value
        else:  # It's a minimizing node
            value = float('inf')
            # Iterate through the children
            for child in children:
                # Recursively call the function for the child node (switch to maximizing)
                value = min(value, minimax_alpha_beta(child, alpha, beta, True))
                # Update beta with the minimum value
                beta = min(beta, value)
                # Prune the tree if necessary (alpha >= beta)
                if alpha >= beta:
                    break
            return value
    else:
        # If the node is not a string, it's a leaf node with a known value
        return node

# Call the minimax algorithm with initial values and store the result
optimal_value = minimax_alpha_beta('B', -float('inf'), float('inf'), True)

# Print the optimal value for the root node 'B'
print("Optimal Value for the Root Node (B):", optimal_value)
