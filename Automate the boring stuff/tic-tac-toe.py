#! python3 
import pprint


the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',\
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',\
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')


printBoard(the_board)