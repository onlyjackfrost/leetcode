class Solution:
    
    
        # time complexity both O(n), and space complexity O(1)  for the following algorithm
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find the single value in nums,  algorithm should have a linear runtime complexity
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1] :
                return nums[i]
        else:
            return nums[len(nums)-1]

    def another_solution(self, nums):
        #using XOR operator 
        output=0
        for num in nums:
            output ^= num   #XOR operator
        return output
