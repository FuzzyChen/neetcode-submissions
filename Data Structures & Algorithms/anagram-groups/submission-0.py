class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in anagramGroups:
                anagramGroups[sortedString] = []
            anagramGroups[sortedString].append(s)
        return list(anagramGroups.values())