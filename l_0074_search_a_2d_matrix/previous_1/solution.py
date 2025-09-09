from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n: int = len(matrix)
        m: int = len(matrix[0])
        l: int = n * m

        l_lhs: int = 0
        l_rhs: int = l - 1

        while l_lhs <= l_rhs:
            l_mid: int = l_lhs + (l_rhs - l_lhs) // 2
            n_mid: int = l_mid // m
            m_mid: int = l_mid % m

            if (mid := matrix[n_mid][m_mid]) == target:
                return True
            elif target > mid:
                l_lhs = l_mid + 1
            else:
                l_rhs = l_mid - 1

        return False
