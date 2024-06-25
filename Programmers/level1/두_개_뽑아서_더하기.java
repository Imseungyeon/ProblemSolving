import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        //중복 방지를 위해 set
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < numbers.length; i++){
            for (int j = i + 1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] answer = new int[set.size()];
        
        //해시셋을 리스트로 변환 (인덱스로 접근 위함)
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        for (int i = 0; i < answer.length; i++){
            answer[i] = list.get(i);
        }

        return answer;
    }
}
