class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        
        # Check if the cleaned list is equal to its reverse
        return cleaned == cleaned[::-1]