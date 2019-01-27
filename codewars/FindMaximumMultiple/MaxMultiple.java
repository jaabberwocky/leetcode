public class MaxMultiple {
  public static int maxMultiple(int divisor, int bound) {
 
    int N = bound;
    while (true) {
      if (N % divisor == 0) {
        return N;
      }
      N -= 1;
    }
  }
}