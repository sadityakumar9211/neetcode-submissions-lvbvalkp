class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Two words are anagrams if they are permutations of each other letters.
        # Break this question in two parts
        # First grouping logic if two strings are anagrams.
        # How we find two strings should belong to same group --> common property.

        # Something that could hold off a set of groups ==> nested data structure
        # Dictionary: (property -> group/list). Property should be hashable

        # Two strings should belong to same group if they are anagrams. Common property 
        # for two strings and the property should be hashable. 

        # property => tuple (hashable) of standard form of all strings

        from collections import defaultdict
        groups = defaultdict(list)

        for word in strs:
            groups[tuple(sorted(word))].append(word)
        
        return list(groups.values())


