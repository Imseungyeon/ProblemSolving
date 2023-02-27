class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for (int i = 0; i < quiz.length; i++){
            String[] arr = quiz[i].split(" ");
            answer[i] = "X";
            if (arr[1].equals("+")){
                if (Integer.valueOf(arr[0]) + Integer.valueOf(arr[2]) == Integer.valueOf(arr[4])) 
                    answer[i] = "O";
            } else{
                if (Integer.valueOf(arr[0]) - Integer.valueOf(arr[2]) == Integer.valueOf(arr[4])) 
                    answer[i] = "O";
            }
        }
        return answer;
    }
}
