class Solution {
    public int solution(String my_string) {
        String[] arr = my_string.split(" ");
        for (int i = 0; i < arr.length; i++){
            if (arr[i].equals("+")){
                arr[i + 1] = Integer.toString(Integer.valueOf(arr[i + 1]) + Integer.valueOf(arr[i - 1]));
            }
            else if (arr[i].equals("-")){
                arr[i + 1] = Integer.toString(Integer.valueOf(arr[i - 1]) - Integer.valueOf(arr[i + 1]));
            }
        }
        return Integer.valueOf(arr[arr.length - 1]);
    }
}
