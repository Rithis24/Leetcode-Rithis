// Last updated: 8/12/2026, 11:52:27 AM
import java.util.Stack;

class Solution {

    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {

            if (ch == '(') {
                stack.push(')');
            } 
            else if (ch == '[') {
                stack.push(']');
            } 
            else if (ch == '{') {
                stack.push('}');
            } 
            else {

                if (stack.isEmpty() || stack.pop() != ch) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}