#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def validline(line):
            nl = filter(lambda x: x!='.',line)
            return len(set(nl))==len(nl)
        for i in xrange(9):
            if (validline(board[i]) and validline(''.join(l[i] for l in board))) is False:
                return False
        for i in xrange(1,9,3):
            for j in xrange(1,9,3):
                tmp = board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]\
                    + board[i][j-1]+board[i][j]+board[i][j+1]\
                    + board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]
                if validline(tmp)==False:
                    return False
        return True    
