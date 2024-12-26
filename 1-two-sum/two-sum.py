class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers and their indices
        num_to_index = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference is in the dictionary
            if diff in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[diff], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]