class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int x = 0, y = 0;
        int answer[] = new int[2];
        for (String move: keyinput){
            
            if (move.equals("left")) x -= 1;
            else if (move.equals("right")) x += 1;
            else if (move.equals("up")) y += 1;
            else if (move.equals("down"))y -= 1;
            
            if (x > board[0] / 2) x = board[0] / 2; 
            else if (x < (board[0] / 2) * -1) x = -1 * (board[0] / 2);
        
            if (y > board[1] / 2) y = board[1] / 2; 
            else if (y < (board[1] / 2) * -1) y = -1 * (board[1] / 2); 
        }
        
        answer[0] = x;
        answer[1] = y;
        return answer;
    }
}
