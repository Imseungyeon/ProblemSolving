class Solution {
    public String solution(int[] food) {
        String answer = "";
        //0 이전의 문자열 만들기
        for(int i = 1; i < food.length; i++){
            answer += Integer.toString(i).repeat(food[i] / 2);
        }
        //reverse() 이용 위한 StringBuilder
        StringBuilder sb = new StringBuilder(answer);
        answer = answer + "0" + sb.reverse().toString();
        return answer;
    }
}
