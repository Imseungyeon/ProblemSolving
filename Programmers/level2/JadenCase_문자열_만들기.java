class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split(" ");
        
        for (int i = 0; i < str.length; i++){
            if (str[i].length() == 0){
                answer += " ";
                continue;            
            }
            answer += str[i].substring(0, 1).toUpperCase();
            answer += str[i].substring(1).toLowerCase();
            if (i != str.length - 1) answer += " ";
        }
        
        int k = s.length() - answer.length();
        for (int j = 1; j <= k; j++){
            answer += " ";
        }
        return answer;
    }
}
