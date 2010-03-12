#!/usr/bin/python
import pyglet
from pyglet.window import key

import mapGen

#create the window
window = pyglet.window.Window(624, 624, caption = "Yeeeehaaaa!")
#center window
window.set_location(window.screen.width/2 - window.width/2, window.screen.height/2 - window.height/2)

#create a rendering batch
batch = pyglet.graphics.Batch()

#load the tiles
tiles = pyglet.image.load('tiles.png')
tiles = pyglet.image.ImageGrid(tiles, 1, 3)

#Generate the map
map = mapGen.createMap(40, 40)
map = mapGen.createPath(map, 800, 20, 20)
map = mapGen.createPath(map, 800, 20, 20)
map = mapGen.createPath(map, 800, 20, 20)

#Parse the map and add tiles to the batch
def renderMap(map):
	tileMap = []
	for y in range(len(map) -1):
		for x in range(len(map[y]) -1):
			if map[y][x] == "1":
				tileMap.append(pyglet.sprite.Sprite(tiles[1], x*16, y*16, batch=batch))
	return tileMap

#render the map
tilemap = renderMap(map)
#render in Terminal
print mapGen.showMap(map, 20, 20, 20)

@window.event
def update(dt):
	window.clear()

pyglet.clock.schedule_interval(update, 1.0/60.0)

@window.event
def on_draw():
	window.clear()
	batch.draw()

window.clear()
pyglet.app.run()