class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> remainderCount(k, 0);
        
        for (int i = 0; i < arr.size(); ++i) {
            int remainder = ((arr[i] % k) + k) % k;  
            remainderCount[remainder]++;
        }
        
        for (int i = 0; i < k; ++i) {
            if (i == 0) {
                if (remainderCount[i] % 2 != 0) {
                    return false;
                }
            }
            else if (remainderCount[i] != remainderCount[k - i]) {
                return false;
            }
        }
        
        return true;
    }
};
