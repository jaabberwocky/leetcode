class Solution {
    
    public static void reverseInPlace(int[] x) {
    int tmp;    

    for (int i = 0; i < x.length / 2; i++) {
        tmp = x[i];
        x[i] = x[x.length - 1 - i];
        x[x.length - 1 - i] = tmp;
    }
}
        
    public int[][] flipAndInvertImage(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            // flip
            reverseInPlace(A[i]);
            
            // inversion
            for (int j = 0; j < A[i].length; j++) {
                if (A[i][j] == 0) {
                    A[i][j] = 1;
                } else {
                    A[i][j] = 0;
                }
            }
        }
        return A;
    }
}