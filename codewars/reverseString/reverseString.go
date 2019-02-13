package kata

// Solution solution
func Solution(word string) string {
	var result string
	for _, char := range word {
		result = string(char) + result
	}
	return result
}
