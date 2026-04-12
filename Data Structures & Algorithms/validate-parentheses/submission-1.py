import collections

class Solution:
    def isValid(self, s: str) -> bool:
        def isBalanced(first, second):
            if first+second in ["()", "{}", "[]"]:
                return True
            else:
                return False

        visited = collections.deque()
        for ch in s:
            if ch in "({[":
                visited.append(ch)
            elif len(visited) > 0 and isBalanced(visited[-1], ch):
                visited.pop()
            else:
                return False
        
        return len(visited) == 0
