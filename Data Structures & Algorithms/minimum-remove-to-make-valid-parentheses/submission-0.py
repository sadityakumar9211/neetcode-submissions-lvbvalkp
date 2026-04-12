class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return True
        
        res = [] 
        cnt = 0 # (o - c)
        for ch in s:
            if ch == '(':
                cnt += 1
                res.append(ch)
            elif ch == ')':
                if cnt > 0:
                    cnt -= 1
                    res.append(ch)
            else:
                res.append(ch)
        
        # remove the extra opening parenthesis from the right.
        # because removing from right makes sense and fit the examples.
        # the ratio of opening/closing ~ 1 when we remove from right
        filtered = []
        for ch in res[::-1]:
            if ch == '(' and cnt > 0:
                cnt -= 1
                continue
            else:
                filtered.append(ch)
        
        return ''.join(filtered[::-1])






            
