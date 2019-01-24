class CountSheep {
    public static String countingSheep(int num) {
      String sheep = "";
      
      for (int i = 1; i <= num; i++) {
        sheep += Integer.toString(i) + " sheep...";
      }
      return sheep;
    }
  }