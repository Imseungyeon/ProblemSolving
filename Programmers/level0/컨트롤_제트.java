class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] str = s.split(" ");
        for (int i = 0; i < str.length; i++){
            if (str[i].equals("Z")){
                str[i] = "0";
                str[i - 1] = "0";
            }
        }
        for (String a : str){
            answer += Integer.parseInt(a);
        }
        return answer;
    }
}
