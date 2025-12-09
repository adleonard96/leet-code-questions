class Solution {
    public long coloredCells(int n) {
        if (n == 1){
            return 1;
        }else if (n == 2){
            return 5;
        } else {
            long result = 5;
            for (int i = 3; i <= n; i++){
                result += (4 * (i - 1)); 
            }
            return result;
        }

    }
}
// 1 
// 5 (4 * i - 1)
// 13 (4 * i - 1) + 5 
// 25 (4 * i - 1) + 13
// 41
