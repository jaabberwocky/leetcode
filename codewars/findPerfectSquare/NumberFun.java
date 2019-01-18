public class NumberFun {
  public static long findNextSquare(long sq) {
      if (isPerfectSquare(sq) == false) {
        return -1;
      } else {
        int smaller = (int) Math.floor(Math.sqrt(sq));
        return (long) Math.pow((double) smaller + 1 , 2.0);
        }
  }
  
  public static boolean isPerfectSquare(long num) {
    int sqrt = (int) Math.sqrt(num);
    if (Math.pow(sqrt,2) == num) {
      return true;
    } else {
      return false;
    }
}
}