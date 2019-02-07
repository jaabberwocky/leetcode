package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	counter := 0
	fibo1 := 1
	fibo2 := 0
	return func() int {
		if counter == 0 {
			counter += 1
			return 0
		} else if counter == 1 {
			counter += 1
			return 1
		} else {
			fibo := fibo1 + fibo2
			fibo2 = fibo1
			fibo1 = fibo
			return fibo
		}
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
