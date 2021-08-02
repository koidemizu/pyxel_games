# -*- coding: utf-8 -*-
#myst.py


import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="MYST")
      #
      pyxel.load('assets/myst.pyxres')
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      #Draw tilemap
      pyxel.bltm(0,0,0,0,16,16,16)

                  
APP()