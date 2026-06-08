class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();
        for (int num : arr1) {
            if (counts.containsKey(num)){
                counts.put(num, counts.get(num)+ 1);
            } else {
                counts.put(num, 1);
            }
        }

        for (int num: arr2) {
            while(counts.containsKey(num)){
                ans.add(num);
                counts.put(num, counts.get(num)-  1);
                if (counts.get(num) == 0){
                    counts.remove(num);
                }
            }
        }

        ArrayList<Integer> remaining = new ArrayList<>();
        for (int num : counts.keySet()) {
            while(counts.get(num) >0) {
                remaining.add(num);
                counts.put(num, counts.get(num) - 1);
            }
        }

        Collections.sort(remaining);

        ans.addAll(remaining);
        return ans.stream().mapToInt(i -> i).toArray();
    }
}