import "sort"

func sortedSquares(A []int) []int {
    var s []int
    
    for _, val := range A {
        s = append(s, val * val)
    }
    
    sort.Ints(s)
    return s
}