class Solution:
    def minimumPushes(self, word: str) -> int:
        word_set = set(word)
        if len(word_set) < 9:
            return len(word)
    
        presses = 0
    
        press_count = {}
        for letter in word_set:
            if press_count.get(word.count(letter)):
                press_count.get(word.count(letter)).append(letter)
            else: 
                press_count[word.count(letter)] = [letter]
        
        push_count = []
        for key in press_count.keys():
            push_count.append(key)
        
        push_count.sort()
        push_count.reverse()
        
        counter = 0
        press_multiplier = 1
        for push in push_count:
            letters = press_count.get(push)
            for letter in letters:
                counter += 1
                presses += press_multiplier * push
                if counter > 7:
                    press_multiplier += 1
                    counter = 0
            
        return presses