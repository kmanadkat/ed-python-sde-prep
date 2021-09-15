from typing import List
from sys import maxsize


# Kadane's Algorithm
# Time - O(n)
# Space - O(1)
def maxSumSubArray(arr: List[int]) -> int:
  # Initialize with most negative num possible
    global_max = -maxsize - 1
    prevMaxEnding = -maxsize - 1

    for ele in arr:
        # Find MaxSum till here - Sum with prevMax or just number
        maxSumEndingHere = max(prevMaxEnding + ele, ele)

        # Update Global Max
        global_max = max(global_max, maxSumEndingHere)

        # Update preMax for next itr
        prevMaxEnding = maxSumEndingHere

    return global_max


print(maxSumSubArray([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(maxSumSubArray([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
