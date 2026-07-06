class Solution {
public:
    int getSum(int a, int b) {
        int mask   = 0xffffffff;
        while (b) {
            int carry = (a&b)<<1;
            a = (a^b)&mask;
            b = carry;
        }
        return a;
    }
};
