class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = r'^[A-Za-z0-9_]+$'
        categories = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid_matches = []
        codes_in_order = []

        for i in range(len(code)):
            if bool(re.match(r'^[A-Za-z0-9_]+$', code[i])) and isActive[i] and businessLine[i] in categories.keys():
                valid_matches.append([code[i], businessLine[i]])
        
        valid_matches = list(sorted(valid_matches, key= lambda x: (categories.get(x[1]), x[0])))
        
        valid_matches = list(map(lambda x: x[0], valid_matches))

        return valid_matches