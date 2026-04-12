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

        dp = [0] * (n+1)
        for i in range(1, n+1):
            # If even --> has same number of 1's as its half number
            # If odd --> contains one more 1 bit than floor(n/2)
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


        