public class Solution
{
    public static String balancedNum(long number)
    {
        String s = Long.toString(number);
        int length = s.length();
        
        if (length < 3) {
          return "Balanced";
        }
        
        long firstHalf = 0;
        long secondHalf = 0;
        char[] firstHalfDigits;
        char[] secondHalfDigits;
                
        if (length % 2 != 0) {
          firstHalfDigits = s.substring(0, length/2).toCharArray();
          secondHalfDigits = s.substring(length/2 + 1, length).toCharArray();
        } else {
          firstHalfDigits = s.substring(0, length/2 - 1).toCharArray();
          secondHalfDigits = s.substring(length/2 + 1, length).toCharArray();
        }
        
        for (int i = 0; i < firstHalfDigits.length; i++) {
          firstHalf += firstHalfDigits[i];
          secondHalf += secondHalfDigits[i];
        }
        
        if (firstHalf == secondHalf) {
          return "Balanced";
        } else {
          return "Not Balanced";
        }
    }
}