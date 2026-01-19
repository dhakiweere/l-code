class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        time    : O(1)
        space   : O(1)
        """
        return str(x) == (str(x))[::-1]