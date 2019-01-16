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

    public static void main(String[] args){
      String s = "this is my shortest word";
      int shortest = findShort(s);
      System.out.println("String: " + s);
      System.out.println("Shortest word length: " + shortest);
    }
}