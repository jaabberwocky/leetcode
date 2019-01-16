public class main{
    
    public static void main(String[] args){
        // shortest word
        System.out.println("ShortestWord.java");
        int returned = ShortestWord.findShort("what is the shortest word here?");
        System.out.println(returned);

        // chocolate
        System.out.println("BreakingChocolateProblem.java");
        System.out.println(Chocolate.breakChocolate(4,5));
    }
}