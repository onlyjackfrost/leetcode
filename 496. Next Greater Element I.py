class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1 are subset in nums2 !!!
        output =[]
        for num1 in nums1:
            for num2 in nums2[nums2.index(num1):] :   
                if num2 > num1:    #check if there are next greater number
                    output += [num2]    #append greater num
                    break
            else:
                output += [-1]     # if not append -1
            
        return output