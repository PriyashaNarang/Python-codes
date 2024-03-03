class Solution(object):
    def lengthOfLastWord(self, s):
        arr=s.split()
        l=len(arr[len(arr)-1])
        return l
