class Solution {
public:
    int countSeniors(vector<string>& details) {
        int len = details.size();
        string newStr;
        int count = 0;
        for(int i=0; i<len; i++){
            newStr = details[i].substr(11, 2);
            if(stoi(newStr) > 60){
                count++;
            }
        }
        return count;
    }
};