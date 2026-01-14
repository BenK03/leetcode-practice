import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # keep only alphanumeric, make lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # reverse
        s_rev = s[::-1]

        if s == s_rev:
            return True
        else:
            return False
        
    # time complexity O(n)