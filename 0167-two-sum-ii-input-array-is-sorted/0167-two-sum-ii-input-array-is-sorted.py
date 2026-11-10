class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
         left=0
         right=len(numbers)-1
         while right > left:

            if numbers[right]+numbers[left]==target:
                return ([left+1,right+1])
                break
            if numbers[right]+numbers[left]>target:
                right=right-1
            if numbers[right]+numbers[left]<target:
                left=left+1
            

        