class Solution {
    public boolean hasDuplicate(int[] nums) {
        
   if(nums.length<1) return false;

   java.util.Arrays.sort(nums);

   int left=0;


   for(int right=1; right<nums.length;right++){

    if(nums[left]== nums[right]){
 return true;
    }

    left++;
   }
 return false;


    }
}