#include <bits/stdc++.h>
using namespace std;

class Solution { 
public: 
    // Function to count digits in 'n' that evenly divide 'n'
    int evenlyDivides(int n) { 
        int count = 0, temp = n; 

        while (n > 0) { 
            int rem = n % 10; // Extract last digit
            n /= 10; // Remove last digit

            // Check for non-zero and divisibility condition
            if (rem != 0 && temp % rem == 0) { 
                count++; 
            }
        }
        return count;
    }
};

int main() { 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; 
    cin >> t; // Number of test cases

    while (t--) { 
        int N; 
        cin >> N; // Input number
        Solution ob; 
        cout << ob.evenlyDivides(N) << "\n"; // Use '\n' instead of endl for faster output
    }
    return 0; 
}