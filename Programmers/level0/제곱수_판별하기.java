class Solution {
    public int solution(int n) {
        int answer = 1;
        if (Math.sqrt(n) - Math.floor(Math.sqrt(n)) != 0) answer = 2;
        return answer;
    }
}
