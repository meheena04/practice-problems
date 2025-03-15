class Solution:
    def firstRepeated(self, arr):
        seen = set()  # Stores seen elements
        for i, num in enumerate(arr):
            if num in seen:
                return i + 1  # Return 1-based index
            seen.add(num)  
        return -1  # If no repeating element found
