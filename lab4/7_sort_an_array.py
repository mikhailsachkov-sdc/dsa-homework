class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heapsort
        n = len(nums)

        # build max heap
        for i in range(n // 2 - 1, -1, -1):
            current = i
            while True:
                largest = current
                left = 2 * current + 1
                right = 2 * current + 2

                if left < n and nums[left] > nums[largest]:
                    largest = left
                if right < n and nums[right] > nums[largest]:
                    largest = right

                if largest != current:
                    nums[current], nums[largest] = nums[largest], nums[current]
                    current = largest
                else:
                    break

        # extract elements from heap
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]

            current = 0
            while True:
                largest = current
                left = 2 * current + 1
                right = 2 * current + 2

                if left < end and nums[left] > nums[largest]:
                    largest = left
                if right < end and nums[right] > nums[largest]:
                    largest = right

                if largest != current:
                    nums[current], nums[largest] = nums[largest], nums[current]
                    current = largest
                else:
                    break

        return nums

