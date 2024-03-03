class Solution(object):
    def isPalindrome(self, x):
        s=0
        x1=x
        while x>0:
            rm=x%10
            s=(s*10)+rm
            x=x//10
        if x1==s:
            return True
        else:
            return False
