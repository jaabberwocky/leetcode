package singlenumber

// taken from leetcode top interview questions - array

func singleNumber(nums []int) int {
	m := make(map[int]int)
	var one int

	for _, num := range nums {
		_, ok := m[num]
		if ok {
			m[num]++
		} else {
			m[num] = 1
		}
	}
	for key, value := range m {
		if value == 1 {
			one = key
		}
	}

	return one

}
