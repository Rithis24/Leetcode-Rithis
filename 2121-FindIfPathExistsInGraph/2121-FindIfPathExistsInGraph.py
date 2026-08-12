# Last updated: 8/12/2026, 11:47:06 AM
import collections
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # Build the adjacency list
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a stack for DFS and a set for visited nodes
        stack = [source]
        visited = {source}

        while stack:
            current_node = stack.pop()

            if current_node == destination:
                return True

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return False