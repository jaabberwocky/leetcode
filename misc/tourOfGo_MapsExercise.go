// solution to exercise:maps
// https://tour.golang.org/moretypes/23

package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	m := make(map[string]int)

	// split string into words
	split := strings.Fields(s)

	for _, char := range split {

		// check membership
		_, ok := m[char]

		if ok == false {
			m[char] = 1
		} else {
			m[char] += 1
		}
	}

	return m
}

func main() {
	wc.Test(WordCount)
}
