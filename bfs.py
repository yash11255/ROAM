graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited_nodes = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue for BFS traversal.

def breadth_first_search(visited, graph, start_node):
    visited.append(start_node)
    queue.append(start_node)
    
    while queue:
        current_node = queue.pop(0)  # Dequeue the first node in the queue.
        print(current_node, end=" ")  # Print the current node.
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Driver Code
print("Breadth-First Search:")
breadth_first_search(visited_nodes, graph, 'A')  # Start BFS from node 'A'
