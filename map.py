from random import *

def printgrid(g):
	print(*map(lambda a:' '.join(map(str,a)), grid), sep='\n')

def randpoint(h,w):
	return (randrange(0,h), randrange(0,w))

deltas = [[-1,0],[1,0],[0,-1],[0,1]]

# def get_edges(s):
# 	sx, sy = s


# h = w = 20
# grid = [[0] * w for _ in range(h)]

# nseeds = 3
# seeds = set((randrange(0, h), randrange(0, w)) for _ in range(nseeds))

# for i, (sx,sy) in enumerate(seeds):
# 	grid[sx][sy] = i+1

# printgrid(grid)

num_rooms = 10

h = w = 10
pos = randpoint(h,w)
vis = set()
while len(vis) < num_rooms:
	shuffle(deltas)
	vis.add(pos)
	sx, sy = pos
	for dx, dy in deltas:
		nx = sx + dx
		ny = sy + dy
		if 0 <= nx < h and 0 <= ny < w:
			pos = (nx, ny)
			break
grid = [['.']*w for _ in range(h)]
for x,y in vis:
	grid[x][y] = 'O'
printgrid(grid)