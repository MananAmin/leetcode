class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        
        //  approach using sort
        return sol1(arr);
        
    }
    
    public List<List<Integer>> sol1(int[] arr){
        
        Arrays.sort(arr);
        
        List<List<Integer>> ans = new ArrayList<>();
        int min = arr[1]-arr[0];
        
        for(int i=0; i<arr.length-1;i++ ){
            
            if(arr[i+1]-arr[i] ==min){
                ans.add(Arrays.asList(arr[i],arr[i+1]));
            }
            else if(arr[i+1]-arr[i] <min){
                ans  = new ArrayList<>();
                ans.add(Arrays.asList(arr[i],arr[i+1]));
                min = arr[i+1]-arr[i];
            }
        }
        
        return ans;
    }
}