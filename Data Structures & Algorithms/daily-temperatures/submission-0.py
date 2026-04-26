class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] # (i, temp)
        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                j, temp = stack.pop()
                result[j] = i - j
            else:
                stack.append((i, temperatures[i]))
        
        return result


        

