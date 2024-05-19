def dfs_count_nodes(graph, start_node):
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)

    dfs(start_node)
    return len(visited)

# Example usage:
# Representing a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Counting nodes visited starting from node 'A'
print(dfs_count_nodes(graph, 'A'))  # Output: 6
