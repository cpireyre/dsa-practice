class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26,0);
        for (char t : tasks) count[t - 'A'] += 1;
        int maxf = *max_element(count.begin(),count.end());
        int maxCount = 0;
        for (int i : count) maxCount += i == maxf;
        int time = (maxf - 1) * (n + 1) + maxCount;
        return max((int)tasks.size(), time);
}
};