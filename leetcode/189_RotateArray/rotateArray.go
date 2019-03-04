package solution_189

func rotate(nums []int, k int) {
	for i := 0; i < k; i++ {
		copy(nums, append([]int{nums[len(nums)-1]}, nums[:len(nums)-1]...))
	}
}
