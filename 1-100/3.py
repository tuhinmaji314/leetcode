class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        ans=0
        for c in s:
            if c in sub:
                i=0
                while sub[i]!=c:
                    i+=1
                sub=sub[i+1:]+c
                
            else:
                sub+=c
            if len(sub)>ans:
                ans=len(sub)
        return ans