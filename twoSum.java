class twoSum {
    //Given an array of integers, find two numbers such that they add up to a specific target number
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
    public static void main(String[] args){
        twoSum obj = new twoSum();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] result = obj.twoSum(nums,target);
        for(int i=0;i<result.length;i++){
            System.out.println(result[i]);
        }
    }
}