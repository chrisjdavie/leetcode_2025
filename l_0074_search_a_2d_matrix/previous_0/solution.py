from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0])
        l: int = m * n - 1
        if l == 0 and matrix[0][0] == target:
            return True

        l_start: int = 0
        l_end: int = l

        for _ in range(100 * 100):
            l_mid: int = (l_start + l_end) // 2
            m_mid: int = l_mid // n
            n_mid: int = l_mid % n

            if matrix[m_mid][n_mid] == target:
                return True
            if target > matrix[m_mid][n_mid]:
                l_start = l_mid + 1
            else:
                l_end = l_mid - 1

            if l_start > l_end:
                break
        else:
            raise ValueError("Tripped limit")

        return False
