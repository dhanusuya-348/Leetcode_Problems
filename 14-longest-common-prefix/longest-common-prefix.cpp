class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len = strs.size();
        if (len == 0){
            return "";
        }
        
        string minstr = strs[0];
        for(int i=1; i<strs.size(); i++) {  
            if(strs[i].length() < minstr.length()) {
                minstr = strs[i];
            }
        }
        
        if(minstr == "") {  
        }
        
        int minlen = minstr.length();
        for(int j=0; j<minlen; j++) {  
            for(int i=0; i<strs.size(); i++) {  
                if(strs[i][j] != minstr[j]) {  
                    return minstr.substr(0, j);  
                }
            }
        }

        return minstr;  
    }
};
