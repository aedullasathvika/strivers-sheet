class Solution:
    # Method to check if the given integer x is a palindrome
    def isPalindrome(self, x: int) -> bool:
        
        # If the number is negative, it can't be a palindrome (negative numbers aren't considered palindromes)
        if x < 0:
            return False
        
        # Reverse the number by converting it to a string, reversing the string, and converting it back to an integer
        t = int(str(x)[::-1])
        
        # Compare the original number with the reversed number
        # If they are the same, the number is a palindrome, so return True
        return x == t