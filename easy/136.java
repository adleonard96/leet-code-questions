package easy;

import java.util.Arrays;

class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);

        int j = 0;
        for (int i = 1; i < nums.length; i++){
            if (nums[j] != nums[i] && j + 1 == i) {
                return nums[j];
            } else if (nums[j] != nums[i]) {
                j = i;
            }
        }
        return nums[j];
    }
}