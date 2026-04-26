class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # this is a monotonically decreasing stack.
        stack = [] # list of indexes for which we haven't found the next higher temperature

        for i in range(n):
            # if we find the higher temperatures than the stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            # 
            stack.append(i)
        
        return result