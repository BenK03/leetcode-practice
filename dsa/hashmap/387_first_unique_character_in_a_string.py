class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = {}

        for char in s:
            if char in hashtable:
                hashtable[char] = hashtable[char] + 1

            else:
                hashtable[char] = 1

        for i, char in enumerate(s):
            if char in hashtable:
                if hashtable[char] == 1:
                    return i
        
        return -1

        # time complexity O(n)

        # Logic
        # Insert into hashtable mapping char to count
        # Loop through again to see the first occuring unique character
        # Then return the index of this character else return -1

