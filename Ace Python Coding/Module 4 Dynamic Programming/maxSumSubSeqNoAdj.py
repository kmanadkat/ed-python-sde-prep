from typing import List


# Time - O(n)
# Space - O(n)
def maxSumSubSeqNoAdj(arr: List[int]) -> int:
    # Handle Edge Cases
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    maxOfFirstTwo = max(arr[0], arr[1])
    maxSums = [arr[0], maxOfFirstTwo]
    globalmax = maxOfFirstTwo

    for i in range(2, len(arr)):
        maxSumTillHere = max(maxSums[i-1], maxSums[i-2] + arr[i])

        globalmax = max(globalmax, maxSumTillHere)

        maxSums.append(maxSumTillHere)

    return globalmax


print(maxSumSubSeqNoAdj([7, 10, 12, 7, 9, 14]))
print(maxSumSubSeqNoAdj([1, 6, 10, 14, -5, -1, 2, -1, 3]))
print(maxSumSubSeqNoAdj([1, -1, 6, -4, 2, 2]))
