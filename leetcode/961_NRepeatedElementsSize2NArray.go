package test

func repeatedNTimes(A []int) int {
	// return the only one found more than once
	m := make(map[int]int)

	for _, num := range A {
		// check for key membership
		_, ok := m[num]
		if ok {
			return num
		} else {
			m[num] = 1
		}
	}
	// default return value; never used
	return 0
}
