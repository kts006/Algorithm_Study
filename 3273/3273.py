import sys

count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
expect = int(sys.stdin.readline())

nums = list(filter(lambda x: x < expect, nums))
nums.sort()

i = 0
j = len(nums) - 1
result = 0

while i < j:
    sum = nums[i] + nums[j]
    if sum == expect:
        i += 1
        j -= 1
        result += 1
    elif sum > expect:
        j -= 1
    elif sum < expect:
        i += 1

print(result)
