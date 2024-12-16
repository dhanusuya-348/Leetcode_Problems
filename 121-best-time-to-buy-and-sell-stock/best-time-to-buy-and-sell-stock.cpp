class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        int mini = INT_MAX;
        int ans = INT_MIN;
        for(int i=0;i<size;i++){
            mini = min(mini, prices[i]);
            ans = max(ans, prices[i]-mini);
        }
        return ans;
    }
};