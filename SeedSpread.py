import pandas as pd
#data is a DataFrame of DEM data
def seedSpreading(data,startpoint,floodLevel):
	xsize, ysize = data.shape
	#if startpoint[0] < xsize and startpoint[1] < ysize and data.iat[startpoint[0],startpoint[1]] < floodLevel:
	stack = set(((startpoint[0], startpoint[1]),))
	points=set()
	mydata=data.copy()
	while stack:
		x, y = stack.pop()
		if mydata.iat[x, y] <floodLevel :
			mydata.iat[x, y] = 11111
			points.add((x , y))
			if x > 0:
				stack.add((x - 1, y))
			if x < (xsize - 1):
				stack.add((x + 1, y))
			if y > 0:
				stack.add((x, y - 1))
			if y < (ysize - 1):
				stack.add((x, y + 1))
			if x > 0 and y> 0:
				stack.add((x - 1, y - 1))
			if x > 0 and y < (ysize - 1):
				stack.add((x - 1, y + 1))
			if x < (xsize - 1) and y > 0:
				stack.add((x + 1, y - 1))
			if x < (xsize - 1) and y < (ysize - 1):
				stack.add((x + 1, y + 1)) 
	return points
