number_grid=[
    [1,2,4],
    [4,7,6],
    [7,8,6]
    ]
print(number_grid[1][0])

#for loops
for r in number_grid:
    print(r)

#nested for loops
for row in number_grid:
    for col in row:
        print(col)