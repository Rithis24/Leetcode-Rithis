# Last updated: 8/12/2026, 11:51:23 AM
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Use a dictionary to store already copied nodes.
        # This maps original_node -> cloned_node.
        # It also serves as a 'visited' set to prevent infinite loops 
        # and redundant copying.
        copies = {}

        def dfs(original_node: Node) -> Node:
            # If the original_node has already been copied, return its 
            # corresponding clone from the copies dictionary.
            if original_node in copies:
                return copies[original_node]

            # Create a new node for the current original_node
            cloned_node = Node(original_node.val)
            # Store this mapping in the dictionary BEFORE processing neighbors.
            # This is critical to handle cycles correctly.
            copies[original_node] = cloned_node

            # Recursively clone the neighbors
            for neighbor in original_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node
        
        # Start the DFS from the given node
        return dfs(node)