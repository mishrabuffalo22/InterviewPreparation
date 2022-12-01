class Solution {
public:
    bool halvesAreAlike(string s) {
        int a = 0, b = 0;
        int n = s.size();
        for(int i = 0; i < n; i++) {
            if(s[i] >= 65 && s[i] <= 91) s[i] = s[i]+32;
            if(i < n/2) {
                if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                    a++;
            } else {
                if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                    b++;
            }
        }

        if(a == b) return true;
        else return false;
    }
};