public class problem4 {

    //Assumptions: nums are not null and has value
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        for(int i = 0; i< n; i++){
            while(nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i]){
                int temp = nums[nums[i]-1];
                nums[nums[i]-1] = nums[i];
                nums[i] = temp;


            }
        }

        for(int i = 0; i < n; i++){
            if(nums[i] != i+1){
                return i+1;
            }
        }
        return n+1;

    }

    public static void main(String[] args){
        Solution test = new Solution();

        //Test 1
        int[] nums1 = new int[]{1,2,0};
        int right1 = 3;
        if(test.firstMissingPositive(nums1) == right1){
            System.out.println("Test1 passed");
        }else{
            System.out.println("Test1 failed!" + "Expected:" + right1 +" but got " + test.firstMissingPositive(nums1));
        }


        //Test 2
        int[] nums2 = new int[]{3,4,-1,1};
        int right2 = 2;
        if(test.firstMissingPositive(nums2) == right2){
            System.out.println("Test2 passed");
        }else{
            System.out.println("Test2 failed!" + "Expected:" + right2 +" but got " + test.firstMissingPositive(nums2));
        }

        //Test 3
        int[] nums3 = new int[]{7,8,9,11,12};
        int right3 = 1;
        if(test.firstMissingPositive(nums3) == right3){
            System.out.println("Test3 passed");
        }else{
            System.out.println("Test3 failed!" + "Expected:" + right3 +" but got " + test.firstMissingPositive(nums3));
        }


    }
}
