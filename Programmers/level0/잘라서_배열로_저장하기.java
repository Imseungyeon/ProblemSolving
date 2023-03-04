class Solution {
    public String[] solution(String my_str, int n) {
        int length = 0;
        if (my_str.length() % n != 0) length = my_str.length() / n + 1;
        else length = my_str.length() / n;
        String[] answer = new String[length];
        
        int cnt = 0;
        for (int i = 0; i < answer.length - 1; i++){
            answer[i] = my_str.substring(cnt, cnt + n);
            cnt += n;
        }
        answer[answer.length - 1] = my_str.substring(cnt);
        
        return answer;
    }
}
