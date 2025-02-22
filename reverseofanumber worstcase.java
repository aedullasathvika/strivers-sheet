class Solution {
    // This method reverses the digits of the input integer x.
    public int reverse(int x) {
        int rev = 0;   // 'rev' will store the reversed number
        int rem;       // 'rem' holds the remainder (the last digit) in each step
        
        // Worst-case scenario: x has the maximum number of digits (10 digits).
        while (x != 0) {
            rem = x % 10;          // Extract the last digit of x
            rev = rev * 10 + rem;  // Append the last digit to 'rev'
            x = x / 10;            // Remove the last digit from x
        }
        
        return rev; // Return the reversed number
    }
    
    // Main method demonstrating the worst-case scenario
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Worst-case input: the largest 32-bit integer (2147483647)
        int worstCaseInput = 2147483647;
        int result = sol.reverse(worstCaseInput);
        System.out.println("Worst Case (Input: " + worstCaseInput + ") - Reversed: " + result);
    }
}