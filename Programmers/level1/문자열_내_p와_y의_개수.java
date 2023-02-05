class Solution {
    boolean solution(String s) {
        boolean answer = false;
        int count = 0;
        s = s.toUpperCase();  

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'P') count++;
            else if (s.charAt(i) == 'Y') count--;
        }
        if (count == 0) answer = true;
        return answer;
    }
}
