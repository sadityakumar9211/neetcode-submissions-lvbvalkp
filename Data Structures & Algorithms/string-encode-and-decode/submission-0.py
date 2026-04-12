class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for el in strs:
            encoded += str(len(el)) + "#" + el
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1

            # skip #
            i += 1
            decoded.append(s[i:i+length])
            i = i + length
        
        return decoded

            
            


            
                

            
