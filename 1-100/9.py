class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1=str(x)
        rev=str1[::-1]
        return str1==rev