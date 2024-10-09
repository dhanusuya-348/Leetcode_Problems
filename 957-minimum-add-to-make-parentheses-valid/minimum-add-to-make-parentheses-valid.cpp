class Solution {
public:
    int minAddToMakeValid(string s) {
        string stack1;
        for(auto c:s){
            if(stack1.empty())
                stack1.push_back(c);
            else if(stack1.back()=='(' && c==')'){
                stack1.pop_back();
            }
            else{
                stack1.push_back(c);
            }
        }        
        return stack1.size();
    }
};