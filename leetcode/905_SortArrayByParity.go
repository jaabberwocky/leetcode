func sortArrayByParity(A []int) []int {
	var odd []int
	var even []int

	for _, val := range A {
		if val%2 == 0 {
			even = append(even, val)
		} else {
			odd = append(odd, val)
		}
	}
	return append(even, odd...)
}