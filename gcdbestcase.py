import math  # Importing the math module to use the gcd function
from typing import List  # Importing List for type hinting in function signature

class Solution:
    # Method to find the Greatest Common Divisor (GCD) of two integers a and b
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        # Calculate the Greatest Common Divisor (GCD) of a and b using math.gcd function
        gcd = math.gcd(a, b)
        
        # Return the GCD in a list
        return [gcd]