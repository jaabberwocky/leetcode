public class XO {
  
    public static boolean getXO (String str) {
      
      int x = 0;
      int o = 0;
      str = str.toLowerCase();
      
      for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) == "x".charAt(0)) {
          x += 1;
        } else if (str.charAt(i) == "o".charAt(0)) {
          o += 1;
        }
      }
      
      if (x == o) {
      return true;
      } else {
      return false;
      }
    }
  }