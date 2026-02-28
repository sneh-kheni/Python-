arpit = [8,"7","5"]
jeel = ["g","a","y"]
sneh = ["s","m","a","r","t"]
friends = [arpit,jeel,sneh]
print(friends)


number_grid = [
    [1,2,3],
    [4,5,6],
    [0,1,2],
    [0,4,5],
    [0],
    ["sneh"]

]

for row in range(len(number_grid)):
    for index in range(len(number_grid[row])) :
        print(number_grid[row][index])
for raw in number_grid:
    for col in raw:
        print(col)
