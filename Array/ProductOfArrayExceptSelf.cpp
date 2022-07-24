// https://leetcode.com/problems/product-of-array-except-self/
// Medium

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left(nums.size());
        int right = 1;

        for(int i = 0; i < nums.size(); i ++) {
            if(i == 0){
                left[i] = 1;
            }
            else {
                left[i] = left[i-1] * nums[i-1];
            }
        }

        for(int i = nums.size() - 1; i >= 0; i --) {
            if(i == nums.size() - 1){
                right = 1;
            }
            else {
                right = right * nums[i+1];
                left[i] = left[i] * right;
            }
        }
        return left;
    }
};
