class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tuple of alphabets in sorted order. 
        dict = collections.defaultdict(list) # key would be the unique thing about all of them in single group!!

        for st in strs:
            t = tuple(sorted(st))
            dict[t].append(st)
        return dict.values()



