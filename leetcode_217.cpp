// duplicates in an array
class Solution {
public:
   
    bool containsDuplicate(vector<int>& nums) {
           set<int> set;

        for(int ele : nums){
                      set.insert(ele);
                        }
                        return (int)set.size() != (int)nums.size();
                        
                       }
                       
                       

               
        };
      
