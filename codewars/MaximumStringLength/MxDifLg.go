package kata

import (
	"math"
)

// MxDifLg is the solution
func MxDifLg(a1 []string, a2 []string) int {
	if len(a1) == 0 || len(a2) == 0 {
		return -1
	}

	// initialise slice to be used to store lengths
	var maxLengths []int

	// iterate to find
	for i := 0; i < len(a1); i++ {

		for j := 0; j < len(a2); j++ {
			diff := math.Abs(float64(len(a1[i]) - len(a2[j])))
			maxLengths = append(maxLengths, int(diff))
		}

	}

	// find max
	largest := 0

	for _, v := range maxLengths {
		if v > largest {
			largest = v
		}
	}

	return int(largest)

}
