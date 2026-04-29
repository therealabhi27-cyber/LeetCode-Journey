class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. Define the dictionary FIRST
        prev_map = {}
        
        # 2. Now start the loop
        for i, n in enumerate(nums):
            diff = target - n
            
            # 3. Check if the complement exists in our map
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # 4. If not found, add current number to map
            prev_map[n] = i
            
        return []