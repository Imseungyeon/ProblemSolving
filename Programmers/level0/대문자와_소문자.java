class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] ch = my_string.toCharArray();
        for (char c: ch){
            if (Character.isUpperCase(c)){
                answer += Character.toLowerCase(c);
            }
            else{
                answer += Character.toUpperCase(c);
            }
        }        
        return answer;
    }
}
