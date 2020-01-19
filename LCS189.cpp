class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        while (k > 0){
        int size = nums.size();
        nums.insert(nums.begin(), nums.back());
        nums.resize(size);
        k--;
        }
    }
};