class Solution {
    public int solution(String s) {
        // 인덱스 이용하여 변환할 것이기 때문에(배열 갯수 줄일 수 있음) 0번째 - zero, 1번째 - one ...
        String[] numbers = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < numbers.length; i++){
            if (s.contains(numbers[i])){
                s = s.replace(numbers[i], Integer.toString(i));
            }
        }
        return Integer.parseInt(s);
    }
}
