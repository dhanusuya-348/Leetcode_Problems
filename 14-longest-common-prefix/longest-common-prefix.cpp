class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len = strs.size();
        if (len == 0){
            return "";
        }
        
        // Find the string with the minimum length
        string minstr = strs[0];
        for(int i=1; i<strs.size(); i++) {  // start from i=1 as minstr is initialized with strs[0]
            if(strs[i].length() < minstr.length()) {
                minstr = strs[i];
            }
        }
        
        if(minstr == "") {  // If the shortest string is empty, return empty
            return "";
        }
        
        int minlen = minstr.length();

        // Compare all strings with the minimum string character by character
        for(int j=0; j<minlen; j++) {  
            for(int i=0; i<strs.size(); i++) {  // Compare the same index across all strings
                if(strs[i][j] != minstr[j]) {  // If there's a mismatch
                    return minstr.substr(0, j);  // Return the common prefix found so far
                }
            }
        }

        return minstr;  // If all characters match for the entire length of minstr
    }
};
