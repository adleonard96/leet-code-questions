class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        option_dict = defaultdict(list)

        for str in strs:
            option_dict["".join(sorted(list(str)))].append(str)

        ans = []

        for key in option_dict.keys():
            ans.append(option_dict[key])

        return ans
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())