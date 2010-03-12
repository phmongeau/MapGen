#!/usr/bin/python

from random import randrange
from copy import deepcopy

def createMap(x, y):
	map = []
	for i in range(y):
		tmp = []
		for n in range(x):
			tmp.append("1")
		map.append(tmp)
	return map


def createPath(map, length,x,y):
	for i in range(length):
		try:
			map[y][x] = "0"		
		except:
			trulu = 1
		x += randrange(-1, 2)
		y += randrange(-1, 2)
	return map

def showMap(map,  x, y, v):
	buffer = ""
	tmp = deepcopy(map)
	tmp[y][x] = "&"
	xmin = x - v
	xmax = x + v
	ymin = y -v
	ymax = y + v
	if xmin < 0:
		xmin = 0
	if xmax > len(tmp[0]):
		xmax = len(tmp[0])
	if ymin < 0:
		ymin = 0
	if ymax > len(tmp):
		ymax = len(tmp)
	
	for i in tmp[ymin:ymax+1]:
		for n in i[xmin:xmax+1]:
			buffer += n + " "
		buffer += "\n"
	return buffer
