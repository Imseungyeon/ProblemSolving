class Solution {
    public int[] solution(long n) {
        int k = (int)Math.log10(n) + 1;
        int[] answer = new int[k];
        for (int i = 0; i < k; i++){
            answer[i] = (int)(n % 10);
            n /= 10;
        }
        return answer;
    }
}
