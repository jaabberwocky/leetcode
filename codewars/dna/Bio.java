public class Bio {
    public String dnaToRna(String dna) {
        if (dna.length() == 0) {
          return "";
        } else {
          dna = dna.replace("T", "U");
          return dna;
        }
        
    } 
}