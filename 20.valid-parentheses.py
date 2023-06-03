#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pd = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in pd.keys():
                stack.append(pd[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        if stack:
            return False
        
        return True

        
# @lc code=end

