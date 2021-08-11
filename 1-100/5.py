class Solution:
    def longestPalindrome(self, s: str) -> str:
        left,right = 0,0
        for i in range(len(s)):
            left,right = max(self.ec(s,i,i),self.ec(s,i,i+1),(left,right),key = lambda x: x[1]-x[0] +1)
            
        
        return s[left:right+1]
                    
    
    def ec(self,s,left,right):
        
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left -= 1
            right += 1
        
        return (left+1,right-1)