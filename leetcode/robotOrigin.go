package solution

// JudgeCircle main function
func JudgeCircle(moves string) bool {
	r := robot{}
	for _, char := range moves {
		dimension, value := convertMove(char)
		switch dimension {
		case "Y":
			r.moveY(value)
		case "X":
			r.moveX(value)
		}
	}

	if r.X == 0 && r.Y == 0 {
		return true
	} else {
		return false
	}
}

type robot struct {
	X int
	Y int
}

// note that *robot pointer arg is needed to refer to the object itself; so that the method will change the struct field
func (r *robot) moveY(y int) {
	r.Y += y
}

func (r *robot) moveX(x int) {
	r.X += x
}

func convertMove(move rune) (string, int) {

	var dimension string
	var value int

	switch move {
	// note that '' is for runes and "" is for strings
	case 'U':
		dimension, value = "Y", 1
	case 'D':
		dimension, value = "Y", -1
	case 'L':
		dimension, value = "X", -1
	case 'R':
		dimension, value = "X", 1
	}

	return dimension, value
}
