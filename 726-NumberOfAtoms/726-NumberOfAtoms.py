# Last updated: 8/12/2026, 11:48:50 AM
import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        
        # Stack to store Counters for different scopes (parentheses)
        # Each element in stack is a Counter mapping atom name to its count
        # The first Counter at stack[0] will accumulate all final counts.
        stack = [collections.Counter()] 
        
        while i < n:
            if formula[i] == '(':
                # Start a new scope, push a new Counter to the stack
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                # End of a scope, pop the current Counter
                current_scope_counts = stack.pop()
                i += 1
                
                # Parse the multiplier after the closing parenthesis
                multiplier = 0
                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
                
                # If no multiplier is specified (e.g., just "(H2O)"), it's 1
                if multiplier == 0:
                    multiplier = 1
                
                # Apply multiplier to all atoms in the popped Counter
                # and add them to the parent scope (top of stack)
                for atom, count in current_scope_counts.items():
                    stack[-1][atom] += count * multiplier
            else: # It's an atom name
                # Parse atom name (starts with uppercase, followed by zero or more lowercase letters)
                start_atom_idx = i
                i += 1 # Move past the initial uppercase letter
                while i < n and formula[i].islower():
                    i += 1
                atom_name = formula[start_atom_idx:i]
                
                # Parse atom count (zero or more digits; if zero, count is 1)
                atom_count = 0
                while i < n and formula[i].isdigit():
                    atom_count = atom_count * 10 + int(formula[i])
                    i += 1
                
                # If no count is specified (e.g., "H" instead of "H1"), it's 1
                if atom_count == 0:
                    atom_count = 1
                
                # Add the atom and its count to the current scope (top of stack)
                stack[-1][atom_name] += atom_count
        
        # The final counts are in the first (and only remaining) Counter on the stack
        final_counts = stack[0]
        
        # Format the output string: sort atoms alphabetically, append count if > 1
        result_parts = []
        for atom in sorted(final_counts.keys()):
            result_parts.append(atom)
            count = final_counts[atom]
            if count > 1:
                result_parts.append(str(count))
                
        return "".join(result_parts)