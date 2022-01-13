T = int(input())
nums = [int(n) for n in input().split(" ")]
nums = sorted(nums)

print(nums[0] * nums[-1])