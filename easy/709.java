package easy;

class Solution {
    public String toLowerCase(String s) {
        StringBuilder letters = new StringBuilder();
        final int MIN_UPPER_CASE = 65;
        final int MAX_UPPER_CASE = 90; 
        for (char c : s.toCharArray()) {
            if ((int) c >= MIN_UPPER_CASE && (int) c <= MAX_UPPER_CASE) {
                int newChar = (int) c + 32;
                c = (char) newChar;
            }
            letters.append(c);
        }

        return letters.toString();
    }
}
