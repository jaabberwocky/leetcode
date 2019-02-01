package kata

import "strings"

// DNAtoRNA : conversion of "T" to "U"
func DNAtoRNA(dna string) string {
	return strings.Replace(dna, "T", "U", -1)
}
