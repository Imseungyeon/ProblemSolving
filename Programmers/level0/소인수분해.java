import java. util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> al = new ArrayList<Integer>();      
        for (int i = 2; i <= n; i++){
            if (n % i == 0){
                int cnt = 0;
                for (int j = 1; j <= i; j++){
                    if (i % j == 0) cnt++;
                }
                if (cnt < 3) al.add(i);      
            }
        }
        return al.stream().mapToInt(Integer::intValue).toArray();
    }
}
