# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:


class Solution:
    def getSmall(self, a, b):
        if a > b:
            return b
        return a

    def maxIncreaseKeepingSkyline(self, grid):
        v = []
        h = []

        nums = len(grid)
        for y in range(nums):
            tmp = grid[y][0]
            for x in range(nums):
                if grid[y][x] > tmp:
                    tmp = grid[y][x]
            h.append(tmp)
        print(h)
        for x in range(nums):
            tmp = grid[0][x]
            for y in range(nums):
                if grid[y][x] > tmp:
                    tmp = grid[y][x]
            v.append(tmp)
        print(v)
        res = 0
        for y in range(nums):
            for x in range(nums):
                print(grid[y][x])
                if grid[y][x] < self.getSmall(v[x], h[y]):
                    print("vertical %d, horizintal %d, value %d" %
                          (v[x], h[y], grid[y][x]))
                    res += self.getSmall(v[x], h[y]) - grid[y][x]
        print(res)


Solution().maxIncreaseKeepingSkyline([
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
])
