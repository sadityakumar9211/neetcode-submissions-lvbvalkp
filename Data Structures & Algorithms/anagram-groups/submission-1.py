class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groupMap = defaultdict(list)
        for st in strs:
            groupMap[tuple(sorted(st))].append(st)
        
        return list(groupMap.values())
        



