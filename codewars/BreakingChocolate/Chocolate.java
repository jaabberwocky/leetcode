public class Chocolate{
  public static int breakChocolate(int n, int m) {
    if (n <= 1 && m <= 1) {
      return 0;
    } else {
      return (n * m) - 1;
  }
  }
  
  // main method to test functionality
  public static void main(String[] args){
      System.out.println("Inputs: 4, 5");
      System.out.println(breakChocolate(4,5));
  }
}