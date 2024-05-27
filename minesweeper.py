#Python program : Minesweeper
#mine = '#' , [(0,3),(0,4),(1,1),(2,2),(3,1),(3,2)] all location of mines
#no_of_rows = 5
#no_of_cols = 5
import numpy as np
def mine_sweeper(mine,no_of_rows,no_of_cols):
#Initialising all values to 0
    grid = [[0  for i in range(no_of_cols)] for j in range(no_of_rows)]

#Assigning the location of all mines.
    for mine_location in mine:
        (mine_row,mine_col) = mine_location #Getting the mine location one by one
        grid[mine_row][mine_col] = '#'  #Placing mines in mines location inside grid
#Geting the row and column range to check preivous and next cells adjacent to mines
        row_range = range(mine_row -1,mine_row + 2)
        col_range = range(mine_col -1,mine_col + 2)  
        for i in row_range:
            for j in col_range:
#checking if 0 is less than current row value and is less than no of rows and 
# if 0 is less than j which is less than no of columns and that cell doesn't have mines
                if (0 <= i< no_of_rows and 0<= j < no_of_cols and grid[i][j] != '#'):
                    grid[i][j] += 1
    return grid                     
#Display the output in matrix form
print (np.matrix ((mine_sweeper([(0,3),(0,4),(1,1),(2,2),(3,1),(3,2)],5,5))))

