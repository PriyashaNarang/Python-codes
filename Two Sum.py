class Solution(object):
    def twoSum(self, nums, target):
        lst=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    lst.append(i)
                    lst.append(j)
                    break
        return lst
