class Solution {
public:
    bool isSameAfterReversals(int num) {
        //int size = num.size();
        if(num==0){
            return true;
        }
        else if(num%10 == 0){
            return false;
        }
        else{
            return true;
        }
        return true;
    }
};