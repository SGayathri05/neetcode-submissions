class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = list(set(nums))
        print(duplicate)
        if len(duplicate) < len(nums):
            return True
        else:
            return False
        

        