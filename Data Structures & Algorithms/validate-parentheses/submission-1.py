class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', '}':'{',']':'['}

        for i in s:
            if i in pair:
                if not stack or stack.pop() != pair[i]:
                    return False
            
            else:
                stack.append(i)
        return not stack