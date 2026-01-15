class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h = {}

        for c in s:
            if c not in h:
                h[c] = 1
            
            else:
                h[c] += 1

        for c in t:
            if c in h:
                h[c] -= 1
            else:
                return False

        for key in h:
            if h[key] != 0:
                return False

        return True
    
    # time complexity O(n) or O(n + m) if string lengths are different