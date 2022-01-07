class Solution {
    public int[] searchRange(int[] nums, int target) {
        if(nums.length==0){
			return new int[]{-1,-1};
		}

		int[] ans =  new int[2];

		ans[0] = leftbinarySearch(nums,0,nums.length,target,-1);
		ans[1] = rightbinarySearch(nums,0,nums.length,target,-1);

		return ans;
        
    }
    
    int rightbinarySearch(int[] array,int left,int right,int search,int ans){
		int mid = left +(right-left)/2;

		if(left<=right &&mid>-1 &&mid<array.length){
			if(array[mid]>search){
				return rightbinarySearch(array,left,mid-1,search,ans);
			}
			else if(array[mid]<search){
				return rightbinarySearch(array,mid+1,right,search,ans);
			}
			else {
				return rightbinarySearch(array,mid+1,right,search,mid);
			}
		}
		return ans;
	}

	int leftbinarySearch(int[] array,int left,int right,int search,int ans){
		int mid = left +(right-left)/2;

		if(left<=right &&mid>-1 &&mid<array.length){
			System.out.println(array[mid]);

			if(array[mid]>search){
				return leftbinarySearch(array,left,mid-1,search,ans);
			}
			else if(array[mid]<search){
				return leftbinarySearch(array,mid+1,right,search,ans);
			}
			else {
				return leftbinarySearch(array,left,mid-1,search,mid);
			}
		}
		return ans;
	}
}