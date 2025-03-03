
def max_consecutive_sum(nums, k):
    if k > len(nums):
        return "k cannot be greater than the length of the list."
    max_sum = sum(nums[ : k])
    current_sum = max_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
print("Maximum sum of", k, "consecutive elements is:", max_consecutive_sum(nums, k))

