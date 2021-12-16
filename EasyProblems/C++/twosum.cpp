#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> m;
        
        for(int i = 0; i < nums.size(); i++) {
            int desired = target - nums.at(i);
            
            if (m.count(desired)) {
                vector<int> solution;
                solution.push_back(m.at(desired));
                solution.push_back(i);
                return solution;
            }
            
            m.insert(pair<int, int>(nums.at(i), i));
        }
        
        return vector<int>();
    }
};