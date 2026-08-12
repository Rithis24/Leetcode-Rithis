# Last updated: 8/12/2026, 11:48:06 AM
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)          # Count occurrences of each number
        return len(freq.values()) == len(set(freq.values()))