class Solution {
public:
    int getSum(int a, int b) {
        long int intmax = 0x7fffffff;
        long int mask   = 0xffffffff;
        while (b) {
            long int carry = (a&b) << 1;
            a = (a^b)&mask;
            b = carry;
        }
        if (a <= intmax) return a;
        return ~(a^mask);
    }
};
