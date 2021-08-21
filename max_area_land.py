curr_land_size = 0

def connected(grid,i,j,visited):
    global curr_land_size

    # checking valid index along with valid land
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or visited[i][j]:
        return

    # mark current land visited 
    visited[i][j] = 1
    curr_land_size+=1

    # goto right and bottom length
    connected(grid, i-1, j, visited)
    connected(grid, i, j-1, visited)
    connected(grid, i+1, j, visited)
    connected(grid, i, j+1, visited)


def land(grid):

    land_count = 0
    max_land_size = 0
    global curr_land_size

    n = len(grid)
    m = len(grid[0])

    visited = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            
            # if land and not visited
            if grid[i][j]==1 and visited[i][j]==0:
                connected(grid,i,j,visited)
                if curr_land_size > max_land_size:
                    max_land_size = curr_land_size
                
                curr_land_size=0
                land_count+=1

    print("Total lands in the grid: ", land_count)
    print("Maximum size land: ", max_land_size)

# given grid: 1-> Land & 0-> Water
grid = [[1,0,0,1],
        [1,1,0,0],
        [1,1,0,0],
        [1,0,1,1]
    ]
        
land(grid)

