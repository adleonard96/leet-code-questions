package easy;

class Solution {
    public boolean judgeCircle(String moves) {
        int[] location = {0,0};
        for (char move : moves.toCharArray()) {
            switch(move) {
                case 'L':
                    location[1]--;
                    break;
                case 'R':
                    location[1]++ ;
                    break;
                case 'U':
                    location[0]++;
                    break;
                case 'D':
                    location[0]--;
                    break;
            }
        }

        return (location[0] == 0 && location[1] == 0); 
    }
}