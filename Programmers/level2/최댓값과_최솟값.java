class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split(" ");
        int[] arr = new int[str.length];
        
        for (int i = 0; i < str.length; i++){
            arr[i] = Integer.valueOf(str[i]);
        }
        
        int maxIdx = 0;
        int minIdx = 0;
        
        for (int i = 0; i < arr.length; i++){
            if (arr[maxIdx] < arr[i]) maxIdx = i;
            if (arr[minIdx] > arr[i]) minIdx = i;
        }
        
        answer = arr[minIdx] + " " + arr[maxIdx];
        
        return answer;
    }
}
