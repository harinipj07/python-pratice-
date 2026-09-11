class Solution:
    def totalNumbers(self, digits):
        nums = [0] * 10
        count = 0

        for i in range(len(digits)):
            nums[digits[i]] += 1

        for i in range(100, 1000, 2):
            evenexist = True

            a = i % 10
            b = (i // 10) % 10
            c = i // 100

            nums[a] -= 1
            if nums[a] < 0:
                evenexist = False

            nums[b] -= 1
            if nums[b] < 0:
                evenexist = False

            nums[c] -= 1
            if nums[c] < 0:
                evenexist = False

            nums[a] += 1
            nums[b] += 1
            nums[c] += 1

            if evenexist:
                count += 1

        return count
