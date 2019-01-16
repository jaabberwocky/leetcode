import java.util.Arrays;

public class ShortestWord {
    public static int findShort(String s) {
        String[] words = s.split(" ");
        int shortestWordLength = words[0].length();
        
        for (int i = 0; i < words.length; i++) {
          if (words[i].length() < shortestWordLength) {
            shortestWordLength = words[i].length();
          }
        }
        return shortestWordLength;
    }
}