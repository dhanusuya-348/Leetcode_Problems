class Solution {
public:
    int clumsy(int n) {
        stack<int> st;
        int i=0;
        int result=0;
        st.push(n--);
        
        while(n>0){
            if(i%4==0){
                st.top() *= n;
            }
            else if(i%4==1){
                st.top() /= n;
            }
            else if(i%4==2){
                st.push(n);
            }
            else{
                st.push(-n);
            }
            i++;
            n--;
        } 

        while(st.size()!=0){
            result+=st.top();
            st.pop();
        } 
        return result;           
    }
};