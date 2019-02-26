package solution771

func numJewelsInStones(J string, S string) int {
	count := 0
	jewels := make(map[rune]bool)

	for _, char := range J {
		if jewels[char] == false {
			jewels[char] = true
		}
	}

	for _, char := range S {
		if jewels[char] == true {
			count++
		}
	}

	return count

}
