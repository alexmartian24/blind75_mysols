class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                return [i,numDict[nums[i]]]
            
            numDict[target-nums[i]] = i

        
        