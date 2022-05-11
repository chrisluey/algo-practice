class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, second = [], -10 ** 9
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while len(stack) > 0 and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])
        return False