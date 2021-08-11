class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
            x=-x
        else:
            sign=1
        num=0
        while x>0:
            num=num*10+x%10
            x=x//10
        if num*sign<-2**31 or num*sign>2**31-1:
            return 0
        else:
            return num*sign