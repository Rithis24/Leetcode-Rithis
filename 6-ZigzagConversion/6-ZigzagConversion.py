# Last updated: 8/12/2026, 11:52:40 AM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        
        current_row = 0
        going_down = False # True if moving down, False if moving up

        for char_code in s:
            rows[current_row].append(char_code)

            # Change direction if at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        # Join the characters in each row and then join the rows
        result = []
        for row_chars in rows:
            result.append("".join(row_chars))
        
        return "".join(result)