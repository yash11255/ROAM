# Define the graph as an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Create a set to keep track of visited nodes.
visited_nodes = set()

# Define a Depth-First Search (DFS) function.
def depth_first_search(graph, start_node):
    # Check if the start_node is already visited.
    if start_node not in visited_nodes:
        print(start_node)  # Print the current node.
        visited_nodes.add(start_node)  # Mark the node as visited.

        # Recursively visit all neighbors of the current node.
        for neighbor in graph[start_node]:
            depth_first_search(graph, neighbor)

# Driver Code
print("Depth-First Search Result:")
depth_first_search(graph, 'A')  # Start DFS from node 'A'
