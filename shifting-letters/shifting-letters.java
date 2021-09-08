class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        
        // suffix sum
        long suffix = 0;                
        char[] ans = new char[shifts.length];
        for(int i = shifts.length -1 ; i >= 0;i--){
            suffix+=shifts[i];
            int ch = s.charAt(i) -'a';
            ans[i] = (char)('a' +(ch + suffix)%26);
        }
        return String.valueOf(ans);
        
    }
}