column_1, row_1 = int(input()), int(input())
column_2, row_2 = int(input()), int(input())

dif_column = column_1 - column_2
dif_row = row_1 - row_2
if dif_row < 0:
    dif_row *= -1
if dif_column < 0:
    dif_column *= -1
if dif_column + dif_row == 3 and column_1 != column_2 and row_1 != row_2:
    print('YES')
else:
    print('NO')
