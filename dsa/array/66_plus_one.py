class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    break

                digits[i] = 0

            else:
                digits[i] = digits[i] + 1
                break

        return digits

    # time complexity O(n)