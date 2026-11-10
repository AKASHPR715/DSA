class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        postfix=1
        prefix=1
        for i in range (0,len(nums)):
            res[i]=prefix
            prefix=nums[i]*prefix
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=nums[i]*postfix
        

       

        return(res)



        