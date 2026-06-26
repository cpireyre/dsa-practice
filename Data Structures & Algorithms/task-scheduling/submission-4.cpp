class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26,0);
        for (char c : tasks) count[c - 'A'] += 1;
        int maxCount = *max_element(count.begin(),count.end());
        int maxf = 0;
        for (int i : count) maxf += i == maxCount;
        int time = (maxCount - 1) * (n + 1) + maxf;
        return max((int)tasks.size(),time);
}
};