class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 -> 0
        1 -> 1 -> 1
        2 -> 10 -> 1
        3 -> 11 -> 2 
        4 -> 100 -> 1
        5 -> 101 -> 2
        6 -> 110 -> 2
        7 -> 111 -> 3
        8 -> 1000 -> 1
        9 -> 1001 -> 2
        10 -> 1010 -> 2
        """

        output = [0] * (n + 1)
        for i in range(n + 1):
            j = i
            while j:
                j = j & (j-1)
                output[i] += 1
        
        return output


        