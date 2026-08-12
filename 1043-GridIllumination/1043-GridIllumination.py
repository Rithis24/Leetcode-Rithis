# Last updated: 8/12/2026, 11:48:26 AM
from collections import defaultdict

class Solution:
    def gridIllumination(self, n, lamps, queries):
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag = defaultdict(int)
        anti = defaultdict(int)

        active = set()

        # Initialize lamps
        for r, c in lamps:
            if (r, c) in active:
                continue
            active.add((r, c))

            rows[r] += 1
            cols[c] += 1
            diag[r - c] += 1
            anti[r + c] += 1

        ans = []

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),  (0, 0),  (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r, c in queries:
            # Check illumination
            if (rows[r] > 0 or
                cols[c] > 0 or
                diag[r - c] > 0 or
                anti[r + c] > 0):
                ans.append(1)
            else:
                ans.append(0)

            # Turn off lamps in 3x3 area
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in active:
                    active.remove((nr, nc))

                    rows[nr] -= 1
                    cols[nc] -= 1
                    diag[nr - nc] -= 1
                    anti[nr + nc] -= 1

        return ans