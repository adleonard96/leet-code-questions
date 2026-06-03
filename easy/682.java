class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String operation: operations) {
            switch (operation) {
                case "C" -> stack.pop();
                case "D" -> stack.push(2 * stack.peek());
                case "+" -> {
                    int top = stack.pop();
                    int newValue = stack.peek() + top;
                    stack.push(top);
                    stack.push(newValue);
                }
                default -> stack.push(Integer.parseInt(operation));
            }


        }
        int result = 0;

        while (!stack.empty()) {
            result += stack.pop();
        }
        return result;
    }
}