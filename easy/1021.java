package easy;

import java.util.ArrayList;

class Solution {
    public String removeOuterParentheses(String s) {
        ArrayList<Character> stack = new ArrayList<>();
        StringBuilder res = new StringBuilder();
        for (char paren: s.toCharArray()) {
            if (stack.isEmpty() || paren == '(') {
                if (stack.isEmpty()) {
                    res.append('(');
                }
                stack.add(paren);
                
            } else {
                if (stack.size() == 1) {
                    stack.remove(0);
                } else {
                    stack.remove(stack.size() - 1);
                    res.append(')');
                }
            }
        }

        return res.toString();
    }
}