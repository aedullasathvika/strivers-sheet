class Solution:
    # Method to check if the given integer x is a palindrome
    def isPalindrome(self, x: int) -> bool:
        
        # Store the original number to compare it later with the reversed number
        t = x
        
        # Initialize revNum to 0. This will store the reversed number
        revNum = 0
        
        # Loop to reverse the digits of the number
        while x > 0:
            # Extract the last digit of x
            r = x % 10
            
            # Remove the last digit from x
            x = x // 10
            
            # Add the extracted digit to revNum, shifting the digits to the left
            revNum = (revNum * 10) + r
        
        # Compare the reversed number with the original number
        # If they are the same, x is a palindrome, so return True
        if t == revNum:
            return True
        else:
            # If they are not the same, return False (it's not a palindrome)
            return False