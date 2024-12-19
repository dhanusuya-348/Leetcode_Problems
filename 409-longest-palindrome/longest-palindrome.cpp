class Solution {
public:
    int longestPalindrome(string s) {
        int oddFrequencyCount = 0;
        unordered_map<char, int> mp;
        for(char ch: s){
            mp[ch]++;
            if(mp[ch]%2 == 1){
                oddFrequencyCount++;
            }
            else{
                oddFrequencyCount--;
            }
        }
        if(oddFrequencyCount>1){
            return s.length() - oddFrequencyCount+1;
        }
        else{
            return s.length();
        }
    }
};