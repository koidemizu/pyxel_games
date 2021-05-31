# -*- coding: utf-8 -*-
#sfv.py


import pyxel

class APP:
  def __init__(self):
      pyxel.init(48, 8, caption="SFV",scale=6)
      #pyxel.init(174, 71, caption="SFV", scale=5)
      #
      pyxel.load('assets/SFV.pyxres')
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      #Draw tilemap
      pyxel.blt(0,0,0,0,32,48,8)
      #pyxel.blt(0,0,1,0,0,174,71)

                  
APP()