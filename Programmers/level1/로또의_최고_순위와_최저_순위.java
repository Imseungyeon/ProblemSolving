class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int count = 0;
        int zeroCount = 0;
        for (int lotto: lottos){
            for (int num: win_nums){
                if (lotto == num) count++;
            }
            if (lotto == 0) zeroCount++;
        }
        answer[0] = 7 - count - zeroCount;
        answer[1] = 7 - count;
        
        if (answer[0] == 7) answer[0] = 6;
        if (answer[1] == 7) answer[1] = 6;
        return answer;
    }
}
