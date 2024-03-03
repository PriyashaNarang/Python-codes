class Solution(object):
    def removeElement(self, nums, val):
        k=nums.count(val)
        i=0
        while i<k:
            nums.remove(val)
            i=i+1
        print(len(nums),"nums = ",nums)
