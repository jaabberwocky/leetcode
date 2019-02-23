package main

import (
	"fmt"
)

func main() {
	i, j := 45, 99

	fmt.Println(i, j)

	// create new pointer p -> i
	var p *int
	p = &i
	fmt.Println(*p)

	// modify i through dereferencing and pointing to the value directly
	*p = 88
	fmt.Println(i)

	// create new pointer to point to pointer p!
	// have to use double "*" to get to the value of i
	pp := &p
	**pp = 128
	fmt.Println(i)
}
