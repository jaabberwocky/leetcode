package kata

func multipleOfIndex(ints []int) []int {
	var returnInts []int

	for index, val := range ints {
		if index == 0 {
			continue
		} else {
			if val%index == 0 {
				returnInts = append(returnInts, val)
			}
		}
	}
	return returnInts
}
