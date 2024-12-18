class Solution {
public:
    string intToRoman(int num) {
        map<int, string> mp;
        mp[1] = "I";
        mp[4] = "IV";
        mp[5] = "V";
        mp[9] = "IX";
        mp[10] = "X";
        mp[40] = "XL";
        mp[50] = "L";
        mp[90] = "XC";
        mp[100] = "C";
        mp[400] = "CD";
        mp[500] = "D";
        mp[900] = "CM";
        mp[1000] = "M";

        string result = "";

        for(auto i=mp.rbegin(); i!=mp.rend(); ++i){
            int a = i->first;
            string b = i->second;
            while(num >= a){
                result += b;
                num -= a;
            }
        }
        return result;
    }
};