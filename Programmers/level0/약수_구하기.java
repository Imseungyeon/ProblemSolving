import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> divisor = new ArrayList<>();
        for (int i = 1; i <= n; i++){
            if (n % i == 0) divisor.add(i);
        }
        Collections.sort(divisor);
        int[] answer = new int[divisor.size()];
        for (int i = 0; i < divisor.size(); i++){
            answer[i] = divisor.get(i);
        }
        return answer;
    }
}
//마지막 ArrayList -> array 변환 과정에서 stream 사용(divisor.stream().mapToInt(x -> x).toArray();)보다 소요시간이 적어 새 array 선언하고 값을 넣는 방법으로 수정
