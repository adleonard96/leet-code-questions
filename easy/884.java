package easy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        HashMap<String, Integer> counter = new HashMap<>();
        Set<String> unique = new HashSet<>();
        for (String word : s1.split(" ")) {
            if (counter.containsKey(word)) {
                unique.remove(word);
            } else {
                counter.put(word, 1);
                unique.add(word); 
            }
        }
        for (String word : s2.split(" ")) {
            if (counter.containsKey(word)) {
                unique.remove(word);
            } else {
                counter.put(word, 1);
                unique.add(word); 
            }
        }
        return unique.toArray(String[]::new);
    }
}