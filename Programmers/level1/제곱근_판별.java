class Solution {
    public long solution(long n) {
        long answer = -1;
        Double d = Math.sqrt(n);
        if (d == Math.floor(d)){
            answer = (long)Math.pow(d + 1, 2);
        }
        return answer;
    }
}
