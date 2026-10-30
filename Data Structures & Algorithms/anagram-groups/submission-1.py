class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        dic = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in dic:
                dic[sorted_str] = [s]
            else:
                dic[sorted_str].append(s)
        res = []
        for s in dic:
            res.append(dic[s])
        return res