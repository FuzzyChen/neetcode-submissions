class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        #can we sort the dictionary?
        l = [] 
        for num in dic:
            l.append([dic[num],num])
        l.sort(key = lambda x: -x[0])
        res = []
        for count,num in l[:k]:
            res.append(num)
        return res