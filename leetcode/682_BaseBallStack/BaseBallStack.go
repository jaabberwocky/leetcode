package solution682

import (
	"strconv"
)

func calPoints(ops []string) int {
	stk := Stack{}
	a := make([]int, 0)
	stk.s = a

	for _, char := range ops {
		val, err := strconv.Atoi(char)
		if err == nil {
			stk.push(val)
			stk.sum = stk.sum + val
		} else {
			if char == "+" {
				x1, x2 := stk.getLastTwo()
				stk.sum = stk.sum + x1 + x2
				stk.push(x1 + x2)
			} else if char == "D" {
				stk.sum = stk.sum + (stk.getLast() * 2)
				stk.push((stk.getLast() * 2))
			} else if char == "C" {
				v := stk.pop()
				stk.sum = stk.sum - v
			} else {
				panic("string not recognised")
			}
		}
	}

	return stk.sum

}

type Stack struct {
	sum int
	s   []int
}

func (s *Stack) push(e int) {
	s.s = append(s.s, e)
}

func (s *Stack) pop() int {
	x := s.s[len(s.s)-1]
	s.s = s.s[:len(s.s)-1]

	return x
}

func (s *Stack) getLastTwo() (int, int) {
	if len(s.s) < 2 {
		return s.s[len(s.s)-1], 0
	}
	x1, x2 := s.s[len(s.s)-1], s.s[len(s.s)-2]
	return x1, x2
}

func (s *Stack) getLast() int {
	x1 := s.s[len(s.s)-1]
	return x1
}
