class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = collections.defaultdict(int)
        hashmap_t = collections.defaultdict(int)

        for ch in s:
            hashmap_s[ch] += 1
        
        for ch in t:
            hashmap_t[ch] += 1
                
        # Compare two dictionaries with keys from english alphabets
        def compare_dict(dict1, dict2):
            if len(dict1.keys()) != len(dict2.keys()):
                return False
            for k1, v1 in dict1.items():
                if dict2[k1] != v1:
                    return False
            
            return True

        return compare_dict(hashmap_s, hashmap_t)
        