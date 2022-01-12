# -*- coding: utf-8 -*-
#images.py


import pyxel

class APP:
  def __init__(self):
      pyxel.init(16, 16, caption="images")
     
      pyxel.load('assets/image.pyxres')
      
      pyxel.mouse(False)
      
      self.x_pos = 0
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if pyxel.btnp(pyxel.KEY_1):
          self.x_pos += 16

  def draw(self):
      pyxel.cls(0)
      
      
      pyxel.blt(0,0,0,0+self.x_pos,0,16,16)
      

                  
APP()