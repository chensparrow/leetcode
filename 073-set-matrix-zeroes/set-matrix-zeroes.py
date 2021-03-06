# -*- coding:utf-8 -*-


# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
#
# click to show follow up.
#
# Follow up:
#
#
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return matrix
        
        # find all (row, col) value 0 and put to stack
        stack = []
        rows = len(matrix)
        cols = len(matrix[0])
        for row in xrange(rows):
            for col in xrange(cols):
                if matrix[row][col] == 0:
                    stack.append((row, col))
        
        # calc 0 rows and cols
        rows_zero = set([x[0] for x in stack])
        cols_zero = set([x[1] for x in stack])
        
        
        # set rows zero and cols zero
        for i in rows_zero:
            matrix[i] = [0] * cols
        
        for j in cols_zero:
            for i in xrange(rows):
                matrix[i][j] = 0
                
        
        
