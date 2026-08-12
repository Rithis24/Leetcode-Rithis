# Last updated: 8/12/2026, 11:48:23 AM
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Create a max-heap using Python's min-heap by storing negative values.
        # This allows us to always pop the largest absolute values (heaviest stones).
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # Continue smashing stones as long as there are at least two stones left.
        while len(max_heap) >= 2:
            # Get the two heaviest stones (which correspond to the two smallest negative values).
            # y is the heaviest, x is the second heaviest.
            y = -heapq.heappop(max_heap) 
            x = -heapq.heappop(max_heap) 

            # Apply the smashing rule
            if x != y:
                # If they are not equal, a new stone with weight y - x is created.
                # Add this new stone (as its negative) back to the heap.
                heapq.heappush(max_heap, -(y - x))
        
        # After the loop, there is at most one stone left in the heap.
        if not max_heap:
            # If the heap is empty, it means all stones were destroyed.
            return 0 
        else:
            # Otherwise, return the weight of the last remaining stone.
            # We negate it back to get the positive weight.
            return -heapq.heappop(max_heap)