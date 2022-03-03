count = int(input())

nums_list = [list(map(int, input().split())) for _ in range(count)]
nums_list.reverse()
triangle = nums_list.pop(0)

while nums_list:
    nums = nums_list.pop(0)

    for idx, num in enumerate(nums):
        nums[idx] = max([nums[idx] + triangle[idx], nums[idx] + triangle[idx+1]])
    triangle = nums
print(triangle[0])
