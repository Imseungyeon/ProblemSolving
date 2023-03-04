class Solution {
    public int solution(int[][] dots) {
        int width = 0;
        int height = 0;
        int idx = 0;
        
        while(width == 0 || height == 0){
            idx++;
            if (dots[0][0] == dots[idx][0]){
                 height = (int)Math.abs(dots[0][1] - dots[idx][1]);
            } 
            if (dots[0][1] == dots[idx][1]){
                width = (int)Math.abs(dots[0][0] - dots[idx][0]);
            }
        }
        return height * width;
    }
}
