import java.util.Arrays;
class Solution {
    public int solution(int[] array, int n) {
        int idx = 0;
        Arrays.sort(array);
        for (int i = 1; i < array.length; i++){
            if (Math.abs(n - array[idx]) > Math.abs(n - array[i])){
                idx = i;
            }
        }
        return array[idx];
    }
}
