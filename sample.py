# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, title="pyxel")
      
      pyxel.load('sample.pyxres')
      
      self.neko_pos = [48, 48] 
      self.neko_muki = 0
      
      pyxel.run(self.update, self.draw)
      
     
  def update(self):
      tile_x = self.neko_pos[0] / 8
      tile_y = self.neko_pos[1] / 8
      if pyxel.btnp(pyxel.KEY_UP):
          tile = pyxel.tilemap(0).pget(tile_x, tile_y - 1)
          if tile == (0, 1):
              self.neko_pos[1] = self.neko_pos[1] - 8
      
      if pyxel.btnp(pyxel.KEY_DOWN):
          tile = pyxel.tilemap(0).pget(tile_x, tile_y + 1)
          if tile == (0, 1):
              self.neko_pos[1] = self.neko_pos[1] + 8
          
      if pyxel.btnp(pyxel.KEY_RIGHT):
          tile = pyxel.tilemap(0).pget(tile_x + 1, tile_y)
          if tile == (0, 1):
              self.neko_pos[0] = self.neko_pos[0] + 8
          self.neko_muki = 0
          
      if pyxel.btnp(pyxel.KEY_LEFT):
          tile = pyxel.tilemap(0).pget(tile_x - 1, tile_y)
          if tile == (0, 1):
              self.neko_pos[0] = self.neko_pos[0] - 8
          self.neko_muki = 1

  def draw(self):
      pyxel.cls(0)

      pyxel.bltm(0, 0, 0, 0, 0, 16, 16)
           
      pyxel.blt(self.neko_pos[0], self.neko_pos[1], 0,
                0 + self.neko_muki * 8, 0, 8, 8, 0)
      
      pyxel.blt(65, 65, 0, 8, 8, 8, 8, 0)
      
      
APP()
