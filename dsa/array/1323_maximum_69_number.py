class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        intList = []

        string = str(num)
        for char in string:
            intList.append(int(char))

        for i in range(len(intList)):
            if intList[i] == 6:
                intList[i] = 9
                break

        ans = ""
        for num in intList:
            ans += str(num)

        ans = int(ans)

        return ans

    # time complexity O(n)