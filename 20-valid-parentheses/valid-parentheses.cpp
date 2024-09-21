class Solution {
public:
    bool isValid(string s) {

        int n = s.length();
        stack<char> stck;

        for(int i=0; i<n; i++)
        {
            if(s[i]=='(' || s[i]=='[' || s[i]=='{'){
                stck.push(s[i]);
            }
            else{
                if(stck.empty()){
                    return false;
                }
                else if(s[i]==')' && stck.top()!='(' || s[i]==']' && stck.top()!='[' ||
                        s[i]=='}' && stck.top()!='{')
                {
                    return false;
                }
                else{
                    stck.pop();
                }
            }
        }
        return stck.empty();        
    }
};