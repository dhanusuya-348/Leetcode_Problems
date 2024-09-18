class Solution {
public:
    bool isPalindrome(int x) {
        int num = x;
        int revnum = 0;
        while(num>0)
        {
            if(revnum>(INT_MAX/10)){
                    printf("Too large");
                    return false;
            }
            revnum = num%10 + revnum*10;
            num = num/10;
        }
        if(x == revnum)
        {
            return true;
        } 
        return false;       
    }
};