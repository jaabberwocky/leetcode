public class Evaporator { 
	
	public static int evaporator(double content, double evap_per_day, double threshold) {
    double thresholdContent = content * threshold / 100;
    int count = 0;
    
    while (content >= thresholdContent) {
      content = content - (content * evap_per_day / 100);
      count += 1;
    }
    
		return count;
	}
}