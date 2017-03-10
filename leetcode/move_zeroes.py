

def moveZeroes(nums):
	zero_cnt = 0
	for i, num in enumerate(nums):
		if num == 0:
			zero_cnt += 1
		else:
			nums[i-zero_cnt] = num
	for i in range(len(nums)-zero_cnt,len(nums)):
		nums[i] = 0

nums = [0,1,0,3,12,0,0,8]

moveZeroes(nums)
print(nums)
