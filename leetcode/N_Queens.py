from itertools import permutations, combinations


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        for s in permutations(range(1, n+1)):
            # print(s)
            for x, y in zip(combinations(s, 2), combinations(range(1, n+1), 2)):
                # print(x, y)
                if x[0]-x[1] == y[0]-y[1] or x[0]-x[1] == y[1]-y[0]:
                    break
            else:
                result.append([(i-1)*'.'+'Q'+(n-i)*'.' for i in s])
        return result


# s = Solution()
# print(s.solveNQueens(4))

    def solveNQueens1(n):
        def DFS(queens, xy_dif, xy_sum):
            print(queens, xy_dif, xy_sum)
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                # 不在同一列，同一对角线
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


import cProfile
# cProfile.run('Solution().solveNQueens(9)')
cProfile.run('solveNQueens1(4)')

