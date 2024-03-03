class Solution(object):
    def reverse(self, x):
        s=0
        if x>(2**31)-1:
            return 0
        elif x<-(2**31):
            return 0
        while x!=0:
            rm=x%10
            s=(s*10)+rm
            x=x//10
        return int(s)
