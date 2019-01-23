import java.util.HashSet;

public class Vowels {

  public static int getCount(String str) {
    int vowelsCount = 0;
    
    // vowels
    HashSet<String> h = new HashSet<>();
    h.add("a");
    h.add("e");
    h.add("i");
    h.add("o");
    h.add("u");
    
    char[] chars = str.toCharArray();
    
    for (char c: chars) {
      if (h.contains(Character.toString(c))) {
        vowelsCount += 1;
      }
    }
    return vowelsCount;
  }

}