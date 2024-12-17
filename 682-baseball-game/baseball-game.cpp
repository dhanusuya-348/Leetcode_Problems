class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        int size = operations.size();
        for(int i=0; i<size; i++){
            if(operations[i]=="+"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.push(a);
                st.push(a+b);
            }
            else if(operations[i]=="D"){
                int c = st.top();
                st.push(c*2);
            }
            else if(operations[i]=="C"){
                st.pop();
            }
            else{
                st.push(stoi(operations[i]));
            }
        }
        int sum=0;
        while(!st.empty()){
            sum += st.top();
            st.pop();
        }
        return sum;        
    }
};