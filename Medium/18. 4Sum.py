class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        def kSum(arr, N, currTarget, result):
            if len(arr) < N or N < 2 or arr[0] * N > currTarget or arr[-1] * N < currTarget:
                return
            elif N == 2:
                l, r = 0, len(arr) - 1
                while l < r:
                    if arr[l] + arr[r] == currTarget:
                        results.append(result + [arr[l], arr[r]])
                        l += 1
                        while l < r and arr[l] == arr[l - 1]:
                            l += 1
                    elif arr[l] + arr[r] < currTarget:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(arr) - N + 1):
                    if i == 0 or (i > 0 and arr[i] != arr[i - 1]):
                        kSum(arr[i + 1:], N - 1, currTarget - arr[i], result + [arr[i]])

        kSum(nums[:], 4, target, [])
        return results
