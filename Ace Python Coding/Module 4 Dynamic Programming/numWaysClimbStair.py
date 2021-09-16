
# Time : O(n)
# Space: O(1)
# Should be 2nd approach - optimizationn
def numWays2(n):
    # Steps 1,2,4
    ways = [0, 1, 2, 3, 6]

    if n < 0:
        return 0

    if n <= 4:
        return ways[n]

    for i in range(5, n+1):
        numWaysForI = ways[1] + ways[3] + ways[4]
        ways[0] = ways[1]
        ways[1] = ways[2]
        ways[2] = ways[3]
        ways[3] = ways[4]
        ways[4] = numWaysForI

    return ways[4]


# Time & Space : O(n)
def numWays(n):
    # Steps 1,2,4
    ways = [0, 1, 2, 3, 6]

    if n < 0:
        return 0

    if n <= 4:
        return ways[n]

    for i in range(5, n+1):
        # Recurrence Relation - s(n) = s(n-1) + s(n-2) + s(n-4)
        numWaysForI = ways[i - 1] + ways[i-2] + ways[i - 4]
        ways.append(numWaysForI)

    return ways[n]


print(numWays(5))
print(numWays(6))
print(numWays(7))
print(numWays(8))

print("Efficient Soln")
print(numWays2(5))
print(numWays2(6))
print(numWays2(7))
print(numWays2(8))
