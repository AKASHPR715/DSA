class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res={}
        c=0
        a=0
        for i in range(len(nums)+1):
            a=a+1
            if (target-nums[i]) in nums[i+1::]:
                x=nums[i+1:].index(target-nums[i])
                print(x)
                x=x+a
                break
            c=c+1
            
        return(c,x)

        