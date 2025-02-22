class Solution {
    // This method reverses the digits of the input integer x.
    public int reverse(int x) {
        int rev = 0;   // 'rev' will store the reversed number
        int rem;       // 'rem' holds the remainder (the last digit) in each step
        
        // Continue looping until x becomes 0.
        // Best-case scenario: x is a single-digit integer, so the loop runs only once.
        while (x != 0) {
            rem = x % 10;         // Extract the last digit of x
            rev = rev * 10 + rem;   // Append the last digit to 'rev'
            x = x / 10;           // Remove the last digit from x
        }
        
        return rev; // Return the reversed number
    }
    
    // Main method demonstrating the best-case scenario
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Best-case input: a single-digit number (e.g., 5)
        int bestCaseInput = 5;
        int result = sol.reverse(bestCaseInput);
        System.out.println("Best Case (Input: " + bestCaseInput + ") - Reversed: " + result);
    }
}