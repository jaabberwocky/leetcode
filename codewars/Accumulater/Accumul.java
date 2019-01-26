public class Accumul {
    
    public static String accum(String s) {
      int counter = 1;
      String completeString = "";
      
      for (char ch: s.toLowerCase().toCharArray()) {
        
        for (int i = 0; i < counter; i++) {
          if (i == 0) {
            completeString += Character.toString(ch).toUpperCase();
            continue;
          }
            completeString += Character.toString(ch);
        }
        if (counter < s.length()) {        
          completeString += "-";
        }
        counter += 1;
    }
    return completeString;
}
}